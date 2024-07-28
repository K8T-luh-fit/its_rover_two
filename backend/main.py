# Example 1 - Control individual LED

from neopixel import NeoPixel
from time import sleep
import random

numpix = 12
strip = NeoPixel(numpix, 0, 14, "RGB")

red = (255, 0, 0)

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.5
strip.brightness(42)
blank = (0, 0, 0)


while True:
    strip.set_pixel(
        random.randint(0, numpix - 1),
        colors_rgb[random.randint(0, len(colors_rgb) - 1)],
    )
    strip.set_pixel(
        random.randint(0, numpix - 1),
        colors_rgb[random.randint(0, len(colors_rgb) - 1)],
    )
    strip.set_pixel(
        random.randint(0, numpix - 1),
        colors_rgb[random.randint(0, len(colors_rgb) - 1)],
    )
    strip.set_pixel(
        random.randint(0, numpix - 1),
        colors_rgb[random.randint(0, len(colors_rgb) - 1)],
    )
    strip.set_pixel(
        random.randint(0, numpix - 1),
        colors_rgb[random.randint(0, len(colors_rgb) - 1)],
    )
    strip.show()
    sleep(delay / 1000000)
    strip.fill((0, 0, 0))
