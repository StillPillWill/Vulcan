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
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg3MDMsInB1ciI6ImJsb2JfaWQifX0=--887b77c9836059ba76946b73c31976fa68c3fe30/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg3MDQsInB1ciI6ImJsb2JfaWQifX0=--2f932eba02bd9fa5a10c02367d6cfa3d895cbd54/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg3MDUsInB1ciI6ImJsb2JfaWQifX0=--4c0ba67b9e6941d0da4ea66517a2d5563299ddb8/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/de3711ee-c4e9-4183-8964-6834d269e27b/video.mp4
- https://lookout.hackclub.com/api/media/77cc3b94-b19f-468d-91d1-cfe3bbb5be71/video.mp4
- https://lookout.hackclub.com/api/media/98b8c0ea-ccd8-4f6e-b0c4-2402b3443dd5/video.mp4
- https://lookout.hackclub.com/api/media/fd625a46-1487-4286-900c-4eaa45d74062/video.mp4

## Entry 2
- ID: 12879
- Author: William
- Created At: 2026-06-10T00:25:44Z

### Content

So I added belt tensioner slots on the arm and then kinda went off on a tangent learning generative design and force simulation. I think these will be pretty critical later on because of the scale of the arm and the fact that I'm using 3D-printed parts. So I decided to experiment with generating and simulating the intermediate segments, which basically just extend the arm's length.  I learned a lot and got some pretty strong results. 
I 3d printed a scaled-down version, and the force distribution is just like the simulations.

![717016137_1340281744707116_4173269289069175901_n.jpg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNTksInB1ciI6ImJsb2JfaWQifX0=--b7b24bd20984a9d44705635d0cdfd03e0286e5fe/717016137_1340281744707116_4173269289069175901_n.jpg)
![Screenshot 2026-06-08 181421.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNjQsInB1ciI6ImJsb2JfaWQifX0=--e5f75372a4c40941e31ef72b977832ba22de069a/Screenshot 2026-06-08 181421.png)
![Screenshot 2026-06-08 232937.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNzEsInB1ciI6ImJsb2JfaWQifX0=--f7926beaf8240326ade90500329b0f868dbaa900/Screenshot 2026-06-08 232937.png)
![Screenshot 2026-06-09 001542.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNzMsInB1ciI6ImJsb2JfaWQifX0=--296dcef7f9e7bd1ff3d66006ca069fde11ec118e/Screenshot 2026-06-09 001542.png)
![Screenshot 2026-06-08 233044.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNzQsInB1ciI6ImJsb2JfaWQifX0=--3310fad9a5deca6f1c447783c8b247d11918e7f6/Screenshot 2026-06-08 233044.png)
![Screenshot 2026-06-08 190918.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNzUsInB1ciI6ImJsb2JfaWQifX0=--e8e4f29309a8b261367348b089aa08ab3b02a070/Screenshot 2026-06-08 190918.png)
![Screenshot 2026-06-08 231731.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAyNzYsInB1ciI6ImJsb2JfaWQifX0=--32da7f32017bc813b706a3f23c36be5dd251f7d6/Screenshot 2026-06-08 231731.png)


### Recording Links

- https://lookout.hackclub.com/api/media/ee156585-6b0e-498a-a100-cd529028b102/video.mp4

## Entry 3
- ID: 12965
- Author: William
- Created At: 2026-06-10T07:50:23Z

### Content

I worked on the upper rotator joint. I don't think I mentioned it before, but I'm going for a design roughly similar to this.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0OTIsInB1ciI6ImJsb2JfaWQifX0=--228b736f3e3ef2265e78ca05eb98c67db394ec92/image.png)

I decided to go with a NEMA 23 for the upper rotator. I briefly considered a NEMA 17 but decided to go with a 23. I will be using 17s for the last two joints tho, mostly for weight effectiveness. This segment should have around 8-10 nm of force, so plenty for these purposes. It uses a 1:5 reduction with a mix of htd 3m and htd 5m belts. I'll be making that upper section cylindrical later on.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0OTQsInB1ciI6ImJsb2JfaWQifX0=--75958e454d9345cdb921d8b01a5395aeeafa9b8a/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0OTYsInB1ciI6ImJsb2JfaWQifX0=--97fd292f5796284ac227ee6f66c8d249bf805721/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/1d4677f4-4e20-4e7e-9618-4d0b0d1ca5f6/video.mp4

## Entry 4
- ID: 13378
- Author: William
- Created At: 2026-06-12T04:32:35Z

### Content

So I went through and made joints 4 cylindrical, for joints 5 and 6, I went with a belted differential design I found, Something like this. 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2NzYsInB1ciI6ImJsb2JfaWQifX0=--5331ae7a7d8e768bebce6463f5b381269bdba328/image.png)
Mines designed for higher loads but besides that its pretty similar.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2NzcsInB1ciI6ImJsb2JfaWQifX0=--e6634b7eeda5e974240742d507c5ba6847b2229d/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2NzgsInB1ciI6ImJsb2JfaWQifX0=--79055fb279af356e22f1d26f441916a9a3210bd0/image.png)
The system is controlled by two NEMA 17s, which, after belting, should produce around 4nm each.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2NzksInB1ciI6ImJsb2JfaWQifX0=--cbfd126bcacc0c47d3992c857c74061b176b00e2/image.png)
 The top part can spin 360 degrees thanks the differential.
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2ODAsInB1ciI6ImJsb2JfaWQifX0=--a325a7115c3dad8cc7884822f28fbfdae5ad7a1f/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE2ODEsInB1ciI6ImJsb2JfaWQifX0=--fad1854bc0a7c2aa5df9b9b98eed99d76a17dd95/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/928164d7-a80f-4953-bbb2-1c9c8a87e490/video.mp4
- https://lookout.hackclub.com/api/media/83259598-74e1-49ab-ba6a-8fd091c64e87/video.mp4

## Entry 5
- ID: 13647
- Author: William
- Created At: 2026-06-13T05:34:38Z

### Content

Uneventful work today. grabbed some of the electronics parts, began working on the base of the arm. Also began work on a phone holding attatchment for the arm
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIzMjksInB1ciI6ImJsb2JfaWQifX0=--82a7e43c9a5c706dc6087f2d26415cfd5c68dfb9/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/46fef5b7-002c-4f1f-aba4-45f65e9537c2/video.mp4
- https://lookout.hackclub.com/api/media/0ea50319-4593-4484-9aee-7351dfdced2e/video.mp4

## Entry 6
- ID: 13920
- Author: William
- Created At: 2026-06-14T08:55:00Z

### Content

Finished up the base and joint 1. And with that the arm is pretty much done. i need to work a little on wire management, and probably just clean up the assembly but its pretty much done. 
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMwNjQsInB1ciI6ImJsb2JfaWQifX0=--6ee19de86ca3af43dc7ee6807718e74744010785/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/ffa07ee4-901a-4e41-9e6b-5934a0520f78/video.mp4

## Entry 7
- ID: 14914
- Author: William
- Created At: 2026-06-18T03:16:37Z

### Content

This time was spent cleaning up the CAD assembly, learning how to make decent-looking renders, as this was my first time using Blender. I also spend most of this time finalizing my filament breakdown to optimize strength for cost. And I decided on almost entirely PETG-CF with some PA6-CF for a couple of the pulleys. Also spent time on general cost optimization. Created a Zine as well. Also began experimenting with custom G-code generation for stronger parts.
![Screenshot 2026-06-16 163128.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzU0MTcsInB1ciI6ImJsb2JfaWQifX0=--f7c63312baf841974059c3a43b4b5e64509f4a4e/Screenshot 2026-06-16 163128.png)


### Recording Links

- https://lookout.hackclub.com/api/media/8efd182e-5b95-4bed-aab0-cbb609fa7522/video.mp4
- https://lookout.hackclub.com/api/media/c04ca39a-7d49-4931-90c8-544e93090e1c/video.mp4
- https://lookout.hackclub.com/api/media/5f1febff-bb13-4cbb-ae75-92e822882ee1/video.mp4
