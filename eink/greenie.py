# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test script for 2.13" 250x122 monochrome display.

Supported products:
  * Adafruit 2.13" Monochrome ePaper Display Breakout
    * https://www.adafruit.com/product/4197
  """

# based on above

import time
import board
import displayio
import adafruit_ssd1675
import terminalio
from adafruit_display_text import label

# make sure display is free in cp
displayio.release_displays()

# This pinout works on a Feather M4 and may need to be altered for other boards.
spi = board.SPI()  # Uses SCK and MOSI
epd_cs = board.D9
epd_dc = board.D10
epd_reset = board.D5
epd_busy = board.D6

# creat the display connection
display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset, baudrate=1000000
)
time.sleep(1)

# some constants
DISPLAY_WIDTH = 250
DISPLAY_HEIGHT = 122
DISPLAY_ROTATION = 270
WHITE = 0xFFFFFF
BLACK = 0x000000

# create display object
display = adafruit_ssd1675.SSD1675(
    display_bus, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rotation=DISPLAY_ROTATION, busy_pin=epd_busy
)

# create display group
g = displayio.Group()

# make a background
background_bitmap = displayio.Bitmap(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)
palette = displayio.Palette(1)
palette[0] = WHITE

# put the background into the display group
bg = displayio.TileGrid(background_bitmap, pixel_shader=palette)
g.append(bg)

# load a bmp file from the circuitpython drive
filename = "/greenie.bmp"

pic = displayio.OnDiskBitmap(filename)
piclayer = displayio.TileGrid(pic, pixel_shader=pic.pixel_shader)
g.append(piclayer)

# write some text

text_group = displayio.Group(scale=2, x=125, y=40)
text = "hello\nworld"
text_area = label.Label(terminalio.FONT, text=text, color=0x000000)
text_group.append(text_area)
g.append(text_group)

# write to the display and refresh
# don't do this too often it is eink!
display.show(g)
display.refresh()
time.sleep(180)

# loop to freeze
while True:
    pass