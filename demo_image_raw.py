"""ESP2in9b v.2 demo (image raw)."""
from time import sleep
from machine import Pin, SPI  # type: ignore
from esp2in9bv2 import Display


def test():
    """Test code."""
    # Try lowering baudrate if you encounter problems
    spi = SPI(2, baudrate=34500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2), busy=Pin(15))
    display.draw_bitmap_raw('images/raspberry_pi_51x64.raw', 38, 116, 51, 64,
                            red=True)
    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()
