"""ESP2in9b v.2 demo (images)."""
from time import sleep
from machine import Pin, SPI  # type: ignore
from esp2in9bv2 import Display


def test():
    """Test code."""
    # Try lowering baudrate if you encounter problems
    spi = SPI(2, baudrate=34500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2), busy=Pin(15))

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
    display.clear_buffers()
    display.draw_bitmap("images/micropythonB126x128.mono", 0, 170, 126, 128,
                        rotate=90)
    display.draw_bitmap("images/micropythonR126x128.mono", 0, 170, 126, 128,
                        rotate=90, red=True)
    display.draw_bitmap("images/micropython175x29.mono", 80, 10, 175, 29,
                        rotate=90, red=True)
    display.present()
    sleep(10)
    display.cleanup()
    print('Done.')


test()
