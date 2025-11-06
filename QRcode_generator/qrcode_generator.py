import qrcode

data = input('enter the text or url: ').strip()
filename = input('enter the filename: ').strip()
select_color = input('which the color: ').lower().strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color=select_color, back_color='white')
image.save(filename)
print('QR code has been created')