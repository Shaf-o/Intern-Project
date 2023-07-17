import qrcode
from PIL import Image


# Add Path or URL to encode data in QRCODE 
url = 'https://github.com/Shaf-o/Intern-Project'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Create Qrcode Image

Image = qr.make_image(fill= 'black', back_color= 'white')

Image.save("QR_Pic.png")
print('Image Created Successfully....')

