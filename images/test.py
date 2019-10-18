# -*- coding: utf-8 -*-
from pyzbar import pyzbar
from PIL import Image, ImageEnhance


def run():
    image = "./71788.jpg"
    img = Image.open(image)
    # img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    # img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    # img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    # img = img.convert('L')#灰度化
    # img.show()
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)

def test():
    users = ['admin', 'mike', 'john', 'lili', 'luxi']
    n = 1
    # del users[-len(users):]
    users=[]
    print(users)

if __name__ == '__main__':
    run()
