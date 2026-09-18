# Nothing is currently tested as I dont have the hardware to do that :(
import time
import board
import busio
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.keys import KC


# PACPAD
#
# Keys:
#   SW1 -> D10
#   SW2 -> D9
#   SW3 -> D8
#   SW4 -> D7
#
# Encoder:
#   A  -> D0
#   B  -> D1
#   SW -> D2
#
# RGB:
#   DIN -> D3
#
# OLED:
#   SDA -> D4
#   SCL -> D5
#
# OLED:
#   SSD1306 128x32
# ============================================================


keyboard = KMKKeyboard()


# 4 KEYS + ENCODER PUSH
# So total as 5 keys 
keys = KeysScanner(
    pins=[
        board.D10,   # SW1
        board.D9,    # SW2
        board.D8,    # SW3
        board.D7,    # SW4
        board.D2,    # Encoder push
    ],
    value_when_pressed=False,
    pull=True,
)


# ROTARY ENCODER

encoder = RotaryioEncoder(
    pin_a=board.D0,
    pin_b=board.D1,
    divisor=4,
)


# KMK combines the scanners.
#
# Key order becomes:
#
#   0 = SW1
#   1 = SW2
#   2 = SW3
#   3 = SW4
#   4 = Encoder push
#   5 = Encoder clockwise
#   6 = Encoder counter-clockwise
#
keyboard.matrix = [
    keys,
    encoder,
]


# KEYMAP

keyboard.keymap = [
    [
        KC.F11,        # SW1 -> Fullscreen
        KC.MPRV,        # SW2 -> Previous track
        KC.MPLY,        # SW3 -> Play and pause

        KC.MNXT,        # SW4 -> Next track

        KC.MUTE,     # Encoder press

        KC.VOLU,     # Encoder clockwise
        KC.VOLD,     # Encoder counter-clockwise
    ]
]


# RGB LEDs

NUM_LEDS = 2

pixels = neopixel.NeoPixel(
    board.D3,
    NUM_LEDS,
    brightness=0.15,
    auto_write=True,
)

# Initial color
pixels[0] = (0, 40, 255) #Deep saturated blue
pixels[1] = (255, 40, 0) #Red

## RAINBOW COLORS (RBG)

def wheel(pos):
    pos = pos & 255 
    
    if pos < 85:
        return (
            255 - pos * 3,
            pos * 3,
            0,
        )
    elif pos < 170:
        pos -= 85 
        return (
            0, 
            255 - pos * 3,
            pos * 3,
        )
    else:
        pos -= 170 
        return (
            pos * 3,
            0,
            255 - pos * 3,
        )

## NOw we make the RGB wave 
wave_position = 0 
last_rgb_update = 0

def update_rgb():
    global wave_position
    global last_rgb_update

    now = time.monotonic()

    # Well update close to 30 times per sec 
    if now - last_rgb_update < 0.03:
        return
    last_rgb_update = now 

    for i in range(NUM_LEDS):

        #Offset each LED so they have different colors
        color_position = (
            wave_position + i * 100 
        ) & 255 

        pixels[i] = wheel(color_position)

    pixels.show()

    # move the rainbow
    wave_position = (wave_position + 3) & 255

#------------
# KMK RGB HOOK
keyboard.before_matrix_scan = update_rgb
    

# Not sure of how to change well check on tht later 

# OLED
# 

# This requires:
#
# adafruit_ssd1306.mpy
#
# to be installed on CIRCUITPY/lib/
#
try:
    import adafruit_ssd1306

    i2c = busio.I2C(
        board.D5,       # SCL
        board.D4,       # SDA
    )

    oled = adafruit_ssd1306.SSD1306_I2C(
        128,
        32,
        i2c,
    )

    oled.fill(0)

    oled.text("PACPAD", 0, 0, 1)
    oled.text("4-Key Macro Pad", 0, 10, 1)
    oled.text("By Lxsh-S", 0, 20, 1)

    oled.show()

except ImportError:
    # Firmware can still run if the OLED library
    # hasn't been installed yet.
    oled = None


if __name__ == "__main__":
    keyboard.go()
