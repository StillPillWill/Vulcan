# Vulcan
*Versatile Utility Ligament for Custom and Numerical-control*

## Overview
Vulcan is a 6-axis, mostly 3D-printed robot arm designed for low cost and high accessibility. It was engineered to be customizable enough for anyone to manufacture, yet robust enough to handle demanding tasks, including CNC or FDM control.

## Design Philosophy: Why Belt Reductions?
Unlike many robot arms that rely on expensive metal gearboxes (which suffer from significant backlash) or 3D-printed planetary gears (which often lack durability and torque), Vulcan utilizes a series of belt reductions.

This system offers several key advantages:
*   **Zero Backlash:** When implemented correctly, belts provide virtually backlash-free movement.
*   **Cost Efficiency:** Belts are significantly more affordable than precision metal gears.
*   **Adaptability:** The design is highly modular. If you need a fast arm, simply reduce the reduction ratio; if you need more strength or precision, increase it. All adjustments can be made by reprinting the pulleys.

## Technical Specifications
The arm's first four axes are driven by reduced NEMA 23 motors. The final two joints (the wrist) utilize two NEMA 17 motors in a belted differential configuration.

| Joint | Torque (Approx. after reduction) |
| :--- | :--- |
| **Joint 1** | 31.25 NM |
| **Joint 2** | 32 NM |
| **Joint 3** | 32 NM |
| **Joint 4** | 10.28 NM |
| **Joint 5 & 6** | 7.2 NM |

<img width="1401" height="2000" alt="Zine" src="https://github.com/user-attachments/assets/749afda4-285b-4e45-8626-389e98f9eeb6" />


<img width="1920" height="1080" alt="Wiring (1)" src="https://github.com/user-attachments/assets/9645b127-c43e-49a3-8ecb-3b90e0440805" />
<img width="860" height="681" alt="Screenshot 2026-06-16 231142" src="https://github.com/user-attachments/assets/3faf460f-fe71-49d1-8282-c8b62e33163d" />

Wiring Diagram
<img width="739" height="456" alt="Screenshot 2026-06-16 204510" src="https://github.com/user-attachments/assets/e3d4da59-5641-4cb9-ac02-e8db7f0ea6ae" />
