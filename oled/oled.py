# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=oled_reset)

# Use for SPI
# spi = board.SPI()
# oled_cs = board.D5
# oled_dc = board.D6
# display_bus = displayio.FourWire(spi, command=oled_dc, chip_select=oled_cs,
#                                 reset=oled_reset, baudrate=1000000)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

splash = displayio.Group()
bitmap = displayio.Bitmap(WIDTH, HEIGHT, 2)
palette = displayio.Palette(2)
palette[0] = 0xFFFFFF
palette[1] = 0x000000

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
splash.append(tile_grid)
display.show(splash)

while True:
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            bitmap[x, y] = 1
        time.sleep(0.005)

    for x in reversed(range(0, WIDTH)):
        for y in reversed(range(0, HEIGHT)):
            bitmap[x, y] = 0
        time.sleep(0.005)
    

# Make the display context
# splash = displayio.Group()
# display.show(splash)

# color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0xFFFFFF  # White

# bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
# splash.append(bg_sprite)

# Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000  # Black
# inner_sprite = displayio.TileGrid(
#     inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
# )
# splash.append(inner_sprite)

# Draw a label
# gtx = displayio.Group(scale = 1)
# text = "Hello World!"
# text_area = label.Label(
#     terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=32 // 2 - 1
# )
# gtx.append(text_area)
# display.show(gtx)