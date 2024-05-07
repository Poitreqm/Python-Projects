#
# Генератор QR-кодов: Реализуйте приложение для создания QR-кодов из текста или URL.
#

import segno
from PIL import Image
from colorit import background, init_colorit

# pip install pillow
# pip install colorit
# pip install segno

init_colorit()  # очищает консоль

print("Hello!")
qr_input = input("Write the text or URL you want to attach to QR-code: ")
qr_name = input("Write the name of the image that will be saved on your computer: ")

qrcode = segno.make(f"{qr_input}", micro=False)
print(qrcode.designator)
qrcode.save(f"{qr_name}.png", scale=15)


image = Image.open(f"{qr_name}.png")
image = image.resize((100, 100))
rgb_im = image.convert("RGB")


for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(background(text=" ", rgb=rgb_im.getpixel((x, y))), end="")

print("Deal!")
print(
    f"Your QR-code was saved to the same folder where this program is located with name {qr_name}.png"
)
