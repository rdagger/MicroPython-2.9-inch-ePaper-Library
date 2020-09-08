"""ESP2in9b v.2 demo (shapes)."""
from time import sleep
from machine import Pin, SPI
from esp2in9bv2 import Display


def test():
    """Test code."""
    spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2), busy=Pin(15))

    display.draw_rectangle(0, 0, 63, 63)
    display.fill_rectangle(5, 5, 53, 53, red=True)

    display.fill_circle(96, 32, 31)
    display.draw_circle(96, 32, 26, invert=True)

    coords = [[0, 106], [60, 106], [11, 70], [30, 128], [49, 70], [0, 106]]
    display.draw_lines(coords)

    display.fill_ellipse(96, 102, 30, 16)
    display.draw_ellipse(96, 102, 16, 30, red=True)

    display.draw_polygon(3, 32, 167, 30, red=True)
    display.fill_polygon(4, 96, 167, 30)
    display.draw_polygon(5, 32, 232, 30)
    display.fill_polygon(6, 96, 232, 30, red=True)

    display.draw_hline(0, 270, 128)
    display.draw_vline(64, 270, 25)
    display.draw_line(64, 295, 127, 270, red=True)
    display.draw_line(64, 295, 0, 270, red=True)

    display.present()

    sleep(10)
    display.clear()
    display.sleep()
    print('Done.')


test()
