"""ESP2in9b v.2 demo (images)."""
from esp2in9bv2 import Display
from machine import Pin, SPI
from time import sleep


def test():
    """Test code."""
    spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(19), cs=Pin(5), rst=Pin(21), busy=Pin(22))

    display.draw_bitmap("images/marqueeB296x64.mono", 64, 0, 296, 64,
                        rotate=90)
    display.draw_bitmap("images/marqueeR296x64.mono", 64, 0, 296, 64,
                        red=True, rotate=90)
    display.draw_bitmap("images/doggy_jet128x64.mono", 0, 0, 128, 64,
                        rotate=90)
    display.draw_bitmap("images/invaders48x36.mono", 13, 200, 48, 36,
                        red=True, invert=True, rotate=90)
    display.present()

    sleep(10)
    display.clear()
    display.sleep()
    print('Done.')


test()
