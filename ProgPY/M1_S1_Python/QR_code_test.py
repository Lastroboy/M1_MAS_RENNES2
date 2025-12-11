import qrcode
img = qrcode.make('https://fr.linkedin.com/in/noa-delaporte')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode_file.png")

