import os
from amzqr import amzqr


def create_amazing_qr():
    print('- Source folder contains source images')
    print('- Result folder contains result images')
    print("Input a filename that exists and be tailed with one of {'.jpg', '.png', '.bmp', '.gif'}!")
    text = input('Enter URL or Text: ')
    input_filename = input('Enter input filename: ')

    version, level, qr_name = amzqr.run(
        words=text,
        picture=f'source/{input_filename}',
        colorized=True,
        save_name=f'result\\{input_filename}',
        save_dir=os.getcwd()
    )

    print("Succeed!")
    print(f'Check out your {version}-{level} QR-code: {qr_name}')


if __name__ == "__main__":
    create_amazing_qr()
