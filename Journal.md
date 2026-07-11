# Robot Arm — Journal Export

- Exported at: 2026-07-11T17:52:01Z
- Project ID: 207
- Entries: 7

## Entry 1
- ID: 12229
- Author: William
- Created At: 2026-06-07T08:34:57Z

### Content

Mostly finished the two main joints, except for the tensioners. Its a 4 stage belt reduction system from a nema 23 stepper motor. I figured that belts were the best type fo drive because they were cheap and had no backlash. Also idk how im gonna print this cause its huge. Anyway with this drive I should have a 1:16 reduction ration giving me around 32 nm of force. I hope the prints are able to handle it
![image](journal%20assets/images/img_1.jpeg)
![image](journal%20assets/images/img_25.jpeg)
![image](journal%20assets/images/img_26.jpeg)


### Recording Links

- [entry1_1.mp4](journal%20assets/entry1_1.mp4)
- [entry1_2.mp4](journal%20assets/entry1_2.mp4)
- [entry1_3.mp4](journal%20assets/entry1_3.mp4)
- [entry1_4.mp4](journal%20assets/entry1_4.mp4)

## Entry 2
- ID: 12879
- Author: William
- Created At: 2026-06-10T00:25:44Z

### Content

So I added belt tensioner slots on the arm and then kinda went off on a tangent learning generative design and force simulation. I think these will be pretty critical later on because of the scale of the arm and the fact that I'm using 3D-printed parts. So I decided to experiment with generating and simulating the intermediate segments, which basically just extend the arm's length.  I learned a lot and got some pretty strong results. 
I 3d printed a scaled-down version, and the force distribution is just like the simulations.

![717016137_1340281744707116_4173269289069175901_n](journal%20assets/images/img_27.jpeg)
![Screenshot 2026-06-08 181421](journal%20assets/images/img_28.jpeg)
![Screenshot 2026-06-08 232937](journal%20assets/images/img_29.jpeg)
![Screenshot 2026-06-09 001542](journal%20assets/images/img_30.jpeg)
![Screenshot 2026-06-08 233044](journal%20assets/images/img_31.jpeg)
![Screenshot 2026-06-08 190918](journal%20assets/images/img_32.jpeg)
![Screenshot 2026-06-08 231731](journal%20assets/images/img_33.jpeg)


### Recording Links

- [entry2_1.mp4](journal%20assets/entry2_1.mp4)

## Entry 3
- ID: 12965
- Author: William
- Created At: 2026-06-10T07:50:23Z

### Content

I worked on the upper rotator joint. I don't think I mentioned it before, but I'm going for a design roughly similar to this.
![image](journal%20assets/images/img_34.jpeg)

I decided to go with a NEMA 23 for the upper rotator. I briefly considered a NEMA 17 but decided to go with a 23. I will be using 17s for the last two joints tho, mostly for weight effectiveness. This segment should have around 8-10 nm of force, so plenty for these purposes. It uses a 1:5 reduction with a mix of htd 3m and htd 5m belts. I'll be making that upper section cylindrical later on.

![image](journal%20assets/images/img_35.jpeg)
![image](journal%20assets/images/img_36.jpeg)


### Recording Links

- [entry3_1.mp4](journal%20assets/entry3_1.mp4)

## Entry 4
- ID: 13378
- Author: William
- Created At: 2026-06-12T04:32:35Z

### Content

So I went through and made joints 4 cylindrical, for joints 5 and 6, I went with a belted differential design I found, Something like this. 
![image](journal%20assets/images/img_37.jpeg)
Mines designed for higher loads but besides that its pretty similar.
![image](journal%20assets/images/img_38.jpeg)
![image](journal%20assets/images/img_39.jpeg)
The system is controlled by two NEMA 17s, which, after belting, should produce around 4nm each.
![image](journal%20assets/images/img_40.jpeg)
 The top part can spin 360 degrees thanks the differential.
![image](journal%20assets/images/img_41.jpeg)
![image](journal%20assets/images/img_42.jpeg)


### Recording Links

- [entry4_1.mp4](journal%20assets/entry4_1.mp4)
- [entry4_2.mp4](journal%20assets/entry4_2.mp4)

## Entry 5
- ID: 13647
- Author: William
- Created At: 2026-06-13T05:34:38Z

### Content

Uneventful work today. grabbed some of the electronics parts, began working on the base of the arm. Also began work on a phone holding attatchment for the arm
![image](journal%20assets/images/img_43.jpeg)


### Recording Links

- [entry5_1.mp4](journal%20assets/entry5_1.mp4)
- [entry5_2.mp4](journal%20assets/entry5_2.mp4)

## Entry 6
- ID: 13920
- Author: William
- Created At: 2026-06-14T08:55:00Z

### Content

Finished up the base and joint 1. And with that the arm is pretty much done. i need to work a little on wire management, and probably just clean up the assembly but its pretty much done. 
![image](journal%20assets/images/img_44.jpeg)


### Recording Links

- [entry6_1.mp4](journal%20assets/entry6_1.mp4)

## Entry 7
- ID: 14914
- Author: William
- Created At: 2026-06-18T03:16:37Z

### Content

This time was spent cleaning up the CAD assembly, learning how to make decent-looking renders, as this was my first time using Blender. I also spend most of this time finalizing my filament breakdown to optimize strength for cost. And I decided on almost entirely PETG-CF with some PA6-CF for a couple of the pulleys. Also spent time on general cost optimization. Created a Zine as well. Also began experimenting with custom G-code generation for stronger parts.
![Screenshot 2026-06-16 163128](journal%20assets/images/img_45.jpeg)


### Recording Links

- [entry7_1.mp4](journal%20assets/entry7_1.mp4)
- [entry7_2.mp4](journal%20assets/entry7_2.mp4)
- [entry7_3.mp4](journal%20assets/entry7_3.mp4)
