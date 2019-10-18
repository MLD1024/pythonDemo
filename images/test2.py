# -*- coding: utf-8 -*-
import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image, ImageEnhance


def get_ewm(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    if os.path.isfile(img_adds):
        # 从本地加载二维码图片
        img = Image.open(img_adds)
    else:
        # 从网络下载并加载二维码图片
        rq_img = requests.get(img_adds).content
        img = Image.open(BytesIO(rq_img))
        img.show()  # 显示图片，测试用

    txt_list = pyzbar.decode(img)

    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        print(barcodeData)


if __name__ == '__main__':
    get_ewm("https://sh.189.cn/QR/code/20004.jpg")