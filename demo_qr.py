"""ESP2in9b v.2 demo (QR Code)."""
from time import sleep
from machine import Pin, SPI  # type: ignore
from esp2in9bv2 import Display
from xglcd_font import XglcdFont
from uQR import QRCode  # https://github.com/i-infra/uQR/


def test():
    """Test code."""
    # Try lowering baudrate if you encounter problems
    spi = SPI(2, baudrate=34500000, sck=Pin(18), mosi=Pin(23))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2), busy=Pin(15))

    neato = XglcdFont('fonts/NeatoReduced5x7.c', 5, 7)

    # Initialize QR code
    qr = QRCode()
    qr.add_data('https://www.rototron.info')
    matrix = qr.get_matrix()

    # Draw QR code to display
    margin = (display.width - len(matrix[0]) * 2) // 2

    for y in range(len(matrix) * 2):  # Scale the image by 2
        for x in range(len(matrix[0]) * 2):
            if matrix[int(y / 2)][int(x / 2)]:
                display.draw_pixel(x + margin, y + margin)

    # Draw caption
    text = "www.rototron.info"
    indent = (display.width - neato.measure_text(text)) // 2
    display.draw_text(indent, (len(matrix) + margin) * 2, text, neato)

    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()
