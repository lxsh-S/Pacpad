# Pacpad

It's a 4-key macro pad with a rotatory encoder and oled display with 2 LEDs, it's built for the Seeduino XIAO with will be running circuitpython and [KMK] (<https://github.com/KMKfw/kmk_firmware>).

  **Current Status: Untested** I have written the firmware for the current setup of the macropad but it hasn't been run on real hardware yet, because I dont have the boards currently and will be receiving them shortly. Please make a PR if you find some issue/bug.

## Hardware

| Function            | Pin |
|---------------------|-----|
| SW1                 | D10 |
| SW2                 | D9  |
| SW3                 | D8  |
| SW4                 | D7  |
| Encoder's A         | D0  |
| Encoder's B         | D1  |
| Encoder's Switch    | D2  |
| NeoPixel data(RGB)  | D3  |
| OLED SDA            | D4  |
| OLED SCL            | D5  |

Our OLED display is 128x32 SSD1306, which we are adressing over I2C

## Current Keymap

| Input                     | Action          |
|---------------------------|-----------------|
| SW1                       | F11(fullscreen) |
| SW2                       | Previous track  |
| SW3                       | Play/Pause      |
| SW4                       | Next track      |
| Encoder push              | Mute            |
| Encoder clockwise         | Vol up          |
| Encoder Anti-clockwiser   | Vol down        |

## TODO

- As the code is completely untested on hardware, I'll try to get that done asap!!
