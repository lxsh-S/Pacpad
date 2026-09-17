# Pacpad

*Pacpad* is a 4-key macropad with a rotatory encoder, an OLED screen and 2LEDs !!!!!!

I've used the KMK firmware for this macropad as python is way more easier than C.

## firmware fucntions

- Media control(prev track, play/pause, next track) with the SW2, SW3, and SW4 keys respectively
- Volume control with the rotatory encoder(volume up, volume down and mute)
- The SW1 key is binded with the F11 key for fullscreen

## PCB

This is my first ever PCB that I made in Kicad. I changed the design like 4 times lol T_T

PCB:
<img width="1081" height="1011" alt="image" src="https://github.com/user-attachments/assets/3bfadada-b3e4-49d0-acba-a2d6f1222de1" />
Schematic:
<img width="1401" height="1193" alt="image" src="https://github.com/user-attachments/assets/84f51506-940f-491e-b894-34e2ef22d891" />
3D:
<img width="1102" height="754" alt="Pacpad (Atlantix) - Autodesk Fusion Personal (Not for Commercial Use)  16-09-2026 10_06_22" src="https://github.com/user-attachments/assets/780a4d7e-60e4-41eb-879f-0d12729668ab" />


## CAD
This case was made in fusion360(I dualbooted win11 for that :)) 
- Top:
<img width="1087" height="564" alt="Pacpad_ (Atlantix) - Autodesk Fusion Personal (Not for Commercial Use)  16-09-2026 10_35_25" src="https://github.com/user-attachments/assets/48e3f989-635a-42e9-9214-b04c3c1e60b5" />

- Bottom: `Note` -> `The hole at the bottom of this design is for a screw that I already have with me (It is to hold the PCB at one place)`
<img width="1029" height="504" alt="Pacpad_ (Atlantix) - Autodesk Fusion Personal (Not for Commercial Use)  16-09-2026 10_35_05" src="https://github.com/user-attachments/assets/1f9fb81a-377b-4479-bd39-15d65e98c81c" />

- Knob: `Used the same as orpheuspad pad`
<img width="598" height="511" alt="Pacpad_CAD_knurled_knob v12 stl at main · lxsh-S_Pacpad — Mozilla Firefox 17-09-2026 21_33_42" src="https://github.com/user-attachments/assets/d655212a-3228-4bb6-8d27-43fb8e8c0b9f" />

- Assembled:
<img width="1141" height="705" alt="Pacpad_ (Atlantix) - Autodesk Fusion Personal (Not for Commercial Use)  16-09-2026 10_34_25" src="https://github.com/user-attachments/assets/d0c0474f-a0f1-4cd7-9fbd-2511bd4d684d" />
<img width="789" height="423" alt="Pacpad_ (Atlantix) - Autodesk Fusion Personal (Not for Commercial Use)  16-09-2026 10_34_35" src="https://github.com/user-attachments/assets/d87f4291-6c74-440f-8ce3-96253ff4a44a" />

## BOM
- 4x MX-Style switches
- 4x Black DSA Keys  
- 1x EC11 Rotatory encoder
- 1x 0.91 inch OLED display
- 2x SK6812MINI-E LEDs
- 1x Seed Xiao RP2040
- PCB made from the gerbers in the repo
