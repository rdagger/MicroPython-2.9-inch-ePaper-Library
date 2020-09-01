"""ESP2in9b v.2 demo (fonts)."""
from xglcd_font import XglcdFont
from esp2in9bv2 import Display
from machine import Pin, SPI
from time import sleep


def test():
    """Test code."""
    spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(19), cs=Pin(5), rst=Pin(21), busy=Pin(22))

    print("Loading fonts.  Please wait.")
    broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    espresso = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    rototron = XglcdFont('fonts/Robotron13x21.c', 13, 21)
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    wendy = XglcdFont('fonts/Wendy7x8.c', 7, 8)

    print("Drawing fonts.")
    text_width = rototron.measure_text("ROTOTRON")
    display.draw_text(64 - text_width // 2, 0, "ROTOTRON", rototron,
                      red=True, rotate=0)
    text_width = espresso.measure_text("Espresso Dolce")
    text_height = espresso.height
    display.draw_text(64 - text_height // 2, 148 - text_width // 2,
                      "Espresso Dolce", espresso, rotate=90)
    display.draw_text(120, 120, "Wendy", wendy, rotate=90)
    display.draw_text(100, 270, "Broadway", broadway, rotate=180)
    display.draw_text(0, 200, "Unispace", unispace, rotate=270)

    display.present()
    sleep(10)
    display.clear()
    display.sleep()
    print("Done.")


test()
