import math

# --- Printer Settings ---
HOTEND_TEMP = 220      # High temp to maintain fluid viscosity for the dovetail squish
BED_TEMP = 70
LAYER_HEIGHT = 0.2
PRINT_SPEED = 450      # 7.5 mm/s (Crucial for fluid-dynamic penetration)
TRAVEL_SPEED = 2400

# --- Geometry: 1" x 1" x 2" (25.4mm x 25.4mm x 50.8mm) ---
SIZE = 25.4            # 1 inch wide/deep
NUM_LAYERS = 254       # 50.8mm / 0.2mm = 254 layers (2 inches tall)

# --- Validated Dovetail Parameters (from dovetail_math.md) ---
AMPLITUDE_W = 0.05     # 0.05mm delta to prevent hydrostatic lock
Z_LIFT = 0.06          # 60 µm shelf, optimized for the Wedge Penetration
PERIOD = 8.0           

# Center on a standard 220x220 Ender 3 V3 SE plate
CENTER_X = 110 - (SIZE / 2)
CENTER_Y = 110 - (SIZE / 2)
current_e = -0.8 

def calc_e(dist, width):
    """
    Calculates volumetric extrusion. 
    Crucially, we ALWAYS use nominal 0.2mm height in this calculation.
    This ensures that when the nozzle is at Z_nom, the excess volume is forced 
    sideways into the Z_lift wedge cavities, forming the dovetail hook.
    """
    fa = math.pi * (1.75 / 2.0) ** 2
    return (dist * width * 0.2 / fa)

def generate_dovetail_layer(layer_index):
    global current_e
    nominal_z = (layer_index + 1) * LAYER_HEIGHT
    gcode = [f"\n; === Layer {layer_index} (Z_nom = {nominal_z:.2f}) ==="]
    
    phase_xy = math.pi if layer_index % 2 == 1 else 0
    STEPS = 30 # Slightly higher resolution for the 1-inch span
    
    # THE ANVIL CONSTRAINT: Print Outer Skin (0), Inner Skin (3), then Cores (1, 2)
    loop_order = [0, 3, 1, 2]
    
    for loop_idx in loop_order:
        # 1. Z-Stagger Logic: Alternate the shelf/hook layer by layer AND loop by loop
        is_elevated = (layer_index + loop_idx) % 2 == 0
        current_z = nominal_z + (Z_LIFT if is_elevated else 0.0)
        
        gcode.append(f"G0 Z{current_z:.3f} F{TRAVEL_SPEED}")
        
        # 2. Calculate Standard Loop Boundaries
        nom_offset = 0.2 + (loop_idx * 0.4)
        c_min = nom_offset
        c_max = SIZE - nom_offset
        corners = [(c_min, c_min), (c_max, c_min), (c_max, c_max), (c_min, c_max)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        # 3. Move to Loop Start
        sx, sy = corners[0]
        start_alpha = math.sin((2 * math.pi / PERIOD) * (sx + sy) + phase_xy)
        wave_offset = 0.5 * AMPLITUDE_W * start_alpha
        
        fx = sx + CENTER_X
        fy = sy + wave_offset + CENTER_Y
        
        gcode.append(f"G0 X{fx:.3f} Y{fy:.3f} F{TRAVEL_SPEED}")
        current_e += 0.8
        gcode.append(f"G1 E{current_e:.5f} F2400 ; Unretract")
        
        prev_fx, prev_fy = fx, fy
        
        # 4. Trace the 4 sides
        for side in range(4):
            dx, dy = dirs[side]
            nx, ny = -dy, dx # Inward normal vector
            p1, p2 = corners[side], corners[(side+1)%4]
            
            for step in range(STEPS):
                frac = (step + 1) / STEPS
                tx = p1[0] + (p2[0] - p1[0]) * frac
                ty = p1[1] + (p2[1] - p1[1]) * frac
                
                # Spatial sine wave
                alpha = math.sin((2 * math.pi / PERIOD) * (tx + ty) + phase_xy)
                wave_offset = 0.5 * AMPLITUDE_W * alpha
                
                curr_fx = tx + nx * wave_offset + CENTER_X
                curr_fy = ty + ny * wave_offset + CENTER_Y
                
                # Truss Width Logic (Opposite phases for interlocking)
                if loop_idx % 2 == 0:
                    w = 0.4 + AMPLITUDE_W * alpha
                else:
                    w = 0.4 - AMPLITUDE_W * alpha
                
                dist = math.hypot(curr_fx - prev_fx, curr_fy - prev_fy)
                current_e += calc_e(dist, w)
                gcode.append(f"G1 X{curr_fx:.3f} Y{curr_fy:.3f} E{current_e:.5f} F{PRINT_SPEED}")
                
                prev_fx, prev_fy = curr_fx, curr_fy
                
        # 5. Retract before jumping to next loop
        current_e -= 0.8
        gcode.append(f"G1 E{current_e:.5f} F2400 ; Retract")
        
    return "\n".join(gcode)

# --- Assemble the G-Code ---
gcode_lines = [
    "; 1x1x2 Inch Dovetail Hook Test Block",
    "; Target: Dimensional Z-Accuracy and Torsional Strength",
    "M104 S{0} ; Start heating hotend".format(HOTEND_TEMP),
    "M140 S{0} ; Start heating bed".format(BED_TEMP),
    "G28",
    "M190 S{0} ; Wait for bed".format(BED_TEMP),
    "M109 S{0} ; Wait for hotend".format(HOTEND_TEMP),
    "G92 E0",
    "G1 E-0.8 F2400 ; Initialize retracted state",
]

for i in range(NUM_LAYERS):
    gcode_lines.append(generate_dovetail_layer(i))

gcode_lines += [
    "\n; --- End Sequence ---",
    "G1 E-2.0 F2400",
    "G91",
    "G0 Z10 F1200",
    "G90",
    "G28 X0",
    "M104 S0",
    "M140 S0",
    "M84",
]

with open("dovetail_1x1x2.gcode", "w") as f:
    f.write("\n".join(gcode_lines))
    
print("Generated dovetail_1x1x2.gcode successfully!")
print(f"Total Layers: {NUM_LAYERS}")
print(f"Calculated Z-Height: {NUM_LAYERS * LAYER_HEIGHT:.2f} mm")