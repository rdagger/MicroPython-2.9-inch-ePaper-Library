"""ESP2in9b v.2 demo (image raw)."""
from time import sleep
from machine import Pin, SPI
from esp2in9bv2 import Display


def test():
    """Test code."""
    spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(19), cs=Pin(5), rst=Pin(21), busy=Pin(22))

    display.draw_bitmap_raw('images/raspberry_pi_51x64.raw', 30, 0, 51, 64,
                            red=False, invert=False)

    display.present()

    sleep(10)
    display.clear()
    display.sleep()
    print('Done.')


test()
