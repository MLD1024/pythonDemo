# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import os


def test(path):
    data = pd.read_excel(path, encoding="utf-8")
    urls = data["url"]
    jurl = []
    i = 0
    for url in urls:
        print i
        i = i + 1
        jurl.append(get_ewm(url))
    data['URL'] = jurl

    # data.loc[16] = [range(1:722)]
    DataFrame(data).to_excel(path, index=False, header=True)
    # df.ix[range(500,1000)]  # 读取指定多行的话，就要在ix[]里面嵌套列表指定行数
    # print("读取指定行的数据：\n{0}".format(data))
    # print


def get_ewm(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    #  去除空格
    url = "".join(img_adds.split())
    # print url
    if os.path.isfile(url):
        # 从本地加载二维码图片
        img = Image.open(url)
    else:
        # 从网络下载并加载二维码图片
        rq_img = requests.get(url).content
        img = Image.open(BytesIO(rq_img))
        # img.show()  # 显示图片，测试用
    txt_list = pyzbar.decode(img)
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        return barcodeData


if __name__ == '__main__':
    test("./data.xlsx")
