# -*- coding: utf-8 -*-
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import openpyxl
import os
import sys

def openpyxl_write(path):
    workbook = openpyxl.load_workbook(path)
    worksheet = workbook.worksheets[0]
    for index, row in enumerate(worksheet.rows):
        url = row[2].value
        if url == "二维码URL" :
            continue
        data_url = ""
        try:
            data_url= get_ewm(url)
        except BaseException as e:
            print  url
        if index==0 :
            row[14].value = "URL"
        else:
            row[14].value = data_url
        if index %200 ==0:
           print index
    workbook.save(filename=path)

def get_ewm(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    if os.path.isfile(img_adds):
        # 从本地加载二维码图片
        img = Image.open(img_adds)
    else:
        # 从网络下载并加载二维码图片
        rq_img = requests.get(img_adds).content
        img = Image.open(BytesIO(rq_img))
        # img.show()  # 显示图片，测试用
    txt_list = pyzbar.decode(img)
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        return barcodeData


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    openpyxl_write("./data2.xlsx")
