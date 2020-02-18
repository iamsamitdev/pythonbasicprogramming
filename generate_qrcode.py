import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("http://www.itgenius.co.th")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")

img.save("myqr.jpg")