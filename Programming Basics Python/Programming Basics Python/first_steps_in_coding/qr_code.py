import pyqrcode
import png
from pyqrcode import QRCode

address = "https://peaksneak.eu/"
url = pyqrcode.create(address)
url.png("peaksneak.png", scale=7)