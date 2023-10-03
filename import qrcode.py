# import package = pip install qrcode,pip install pillow

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 4,
                   )

qr.add_data("https://www.amazon.in/")
qr.make(fit=True)

#create an image from the QR code instance
img = qr.make_image(fill_color="black", background_color="white")
#save the image
img.save("amazon.png")