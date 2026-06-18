import math

# --- V4 INTERLOCK CONFIGURATION ---
FILAMENT_DIA = 1.75
LAYER_HEIGHT = 0.2
LINE_WIDTH = 0.4
NUM_WALLS = 5           # 5 perimeters to ensure a dense, strong hook

# Volumetric Wave Parameters
WAVE_LENGTH = 3.0       # mm distance between Pegs and Sockets
AMPLITUDE = 0.85        # 85% variance for extreme interlock

# Vertical J-Hook Dimensions (Approx 1 inch / 25.4mm total height)
HEIGHT_BASE = 5.0       # Bottom U-turn of the J (Z = 0 to 5)
HEIGHT_TIP = 10.0       # Top of the short hook tip (Z = 5 to 10)
HEIGHT_TOTAL = 25.4     # Top of the main stem (Z = 10 to 25.4)

# Cross-sectional boundaries (X, Y)
WIDTH_TOTAL = 15.0
DEPTH = 6.0
STEM_WIDTH = 5.0
TIP_WIDTH = 5.0

SEGMENT_RES = 0.1       # Micro-stepping resolution for the wave

def get_filament_length(volume):
    area = math.pi * ((FILAMENT_DIA / 2.0) ** 2)
    return volume / area

def get_rect_perimeters(x_min, x_max, y_min, y_max, walls):
    """Generates concentric rectangular paths inset from the given boundaries."""
    perimeters = []
    for w in range(walls):
        inset = (w * LINE_WIDTH) + (LINE_WIDTH / 2.0)
        x0 = x_min + inset
        x1 = x_max - inset
        y0 = y_min + inset
        y1 = y_max - inset
        
        # If inset pushes walls too close to the center, stop generating
        if x0 >= x1 or y0 >= y1:
            break
            
        # Rectangle path: Start BL -> BR -> TR -> TL -> BL
        path = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
        perimeters.append(path)
    return perimeters

def build_vertical_gcode():
    gcode = []
    gcode.append("; --- V4 VERTICAL J-HOOK: Z-ADHESION TEST ---")
    gcode.append("G28 ; Home axes")
    gcode.append("G90 ; Absolute positioning")
    gcode.append("M82 ; Absolute extrusion mode")
    gcode.append("G92 E0 ; Reset Extruder")
    gcode.append("G1 Z5.0 F3000 ; Lift Z")
    gcode.append("M109 S220 ; Wait for Hotend (Ensure high flow!)")
    gcode.append("M900 K0 ; Disable Marlin Linear Advance")
    gcode.append("SET_PRESSURE_ADVANCE ADVANCE=0 ; Disable Klipper PA")
    
    absolute_e = 0.0
    total_layers = int(HEIGHT_TOTAL / LAYER_HEIGHT)
    
    for layer_idx in range(total_layers):
        z_height = (layer_idx + 1) * LAYER_HEIGHT
        gcode.append(f"\n; --- LAYER {layer_idx} (Z = {z_height:.2f}) ---")
        gcode.append(f"G1 Z{z_height:.2f} F1200")
        
        # Determine which parts of the J-hook exist at this Z-height
        shapes = []
        if z_height <= HEIGHT_BASE:
            # Base of the J (Full width)
            shapes.append(get_rect_perimeters(0, WIDTH_TOTAL, 0, DEPTH, NUM_WALLS))
        elif z_height <= HEIGHT_TIP:
            # Split section: Main Stem AND Hook Tip
            shapes.append(get_rect_perimeters(0, STEM_WIDTH, 0, DEPTH, NUM_WALLS))
            shapes.append(get_rect_perimeters(WIDTH_TOTAL - TIP_WIDTH, WIDTH_TOTAL, 0, DEPTH, NUM_WALLS))
        else:
            # Top section: Main Stem only
            shapes.append(get_rect_perimeters(0, STEM_WIDTH, 0, DEPTH, NUM_WALLS))
            
        for shape_perimeters in shapes:
            for wall_idx, path in enumerate(shape_perimeters):
                gcode.append(f"; Perimeter {wall_idx}")
                
                # The V4 Phase Matrix Equation
                phase_shift = (layer_idx + wall_idx) * math.pi
                
                # Travel to start of perimeter
                gcode.append(f"G1 X{path[0][0]:.3f} Y{path[0][1]:.3f} F3000")
                
                total_distance = 0.0
                
                # Discretize the rectangular path into SEGMENT_RES chunks
                for i in range(1, len(path)):
                    x_start, y_start = path[i-1]
                    x_end, y_end = path[i]
                    
                    line_len = math.sqrt((x_end - x_start)**2 + (y_end - y_start)**2)
                    steps = max(1, int(line_len / SEGMENT_RES))
                    
                    dx = (x_end - x_start) / steps
                    dy = (y_end - y_start) / steps
                    
                    curr_x = x_start
                    curr_y = y_start
                    
                    for step in range(steps):
                        curr_x += dx
                        curr_y += dy
                        total_distance += SEGMENT_RES
                        
                        nominal_vol = SEGMENT_RES * LINE_WIDTH * LAYER_HEIGHT
                        wave_multiplier = 1.0 + AMPLITUDE * math.sin((2 * math.pi * total_distance / WAVE_LENGTH) + phase_shift)
                        
                        target_vol = nominal_vol * wave_multiplier
                        absolute_e += get_filament_length(target_vol)
                        
                        # Very slow feedrate (600mm/min = 10mm/s) to handle extreme volume surges
                        gcode.append(f"G1 X{curr_x:.3f} Y{curr_y:.3f} E{absolute_e:.4f} F600")

    gcode.append("\n; --- END SCRIPT ---")
    gcode.append("G1 Z+10 F3000")
    gcode.append("G28 X Y")
    gcode.append("M104 S0 ; Turn off extruder")
    gcode.append("M84 ; Disable motors")
    
    with open("V4_Vertical_Hook.gcode", "w") as f:
        f.write("\n".join(gcode))
        
    print("V4_Vertical_Hook.gcode generated successfully.")

if __name__ == "__main__":
    build_vertical_gcode()