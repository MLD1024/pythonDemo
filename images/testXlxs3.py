# -*- coding: utf-8 -*-
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import openpyxl
import os
import sys
import threadpool

i = 0


def openpyxl_read(path):
    workbook = openpyxl.load_workbook(path)
    worksheet = workbook.worksheets[0]
    pool = threadpool.ThreadPool(20)
    data = []
    for index, row in enumerate(worksheet.rows):
        data.append({'index': index, 'url': row[2].value})
        openpyxl_write({'index': index, 'url': row[2].value})
        # if len(data) == 10:
        #     print index
        #     requests = threadpool.makeRequests(openpyxl_write, data)
        #     [pool.putRequest(req) for req in requests]
        #     pool.wait()
        #     del data[-len(data):]

def openpyxl_write(data):
    workbook = openpyxl.load_workbook("./data0.xlsx")
    worksheet = workbook.worksheets[0]
    url=data["url"]
    index=data["index"]
    if url != "二维码URL":
        try:
            data_url = get_ewm(url)
            list( worksheet.rows)[index][14].value = data_url
        except BaseException as e:
            try:
                data_url = get_ewm(url)
                list( worksheet.rows)[index][14].value = data_url
            except  BaseException as e:
                print  url
    workbook.save("./data0.xlsx")

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
    openpyxl_read("./data2.xlsx")
