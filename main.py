import os
from amzqr import amzqr
from PIL import Image, ImageOps


img_size = 1024
default_border_size = 7.5


def get_image(filename):
    img = Image.open(f'source/{filename}')
    img_alpha = img.convert("RGBA")
    return img_alpha


def resize_image(img):
    img.thumbnail((1024, 1024), Image.ANTIALIAS)


def add_transparent_frame(filename, img, border_size):
    img_border = ImageOps.expand(img, border=round(img_size * border_size / 100))
    img_border.save(f'result/{filename}')


def create_amazing_qr():
    print('- Source folder contains source images')
    print('- Result folder contains result images')
    print("Input a filename that exists and be tailed with one of {'.jpg', '.png', '.bmp', '.gif'}!")
    text = input('URL or Text: ')
    filename = input('Filename: ')
    border_size = input("Border size (in percent): ")
    border_size = float(border_size) if border_size else default_border_size

    img = get_image(filename)
    resize_image(img)
    # img.save(f'test.png')

    add_transparent_frame(filename, img, border_size)

    version, level, qr_name = amzqr.run(
        words=text,
        picture=f'result/{filename}',
        colorized=True,
        save_name=f'result\\{filename}',
        save_dir=os.getcwd()
    )

    print("Succeed!")
    print(f'Check out your {version}-{level} QR-code: {qr_name}')


if __name__ == "__main__":
    create_amazing_qr()
