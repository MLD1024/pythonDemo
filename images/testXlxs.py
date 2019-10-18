# -*- coding: utf-8 -*-
import xlrd
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import copy
import openpyxl
import os
import sys
# from  multiprocessing import Pool
import threadpool
import threading
def red(path):
    workbook = xlrd.open_workbook(path, encoding_override="ascii")
    # 索引到第X个工作表
    sheet = workbook.sheet_by_index(0)
    # 查看有多少行
    print(sheet.nrows)
    # 查看有多少列
    print(sheet.ncols)

    # pool = Pool(5)
    # 获取单元格内容
    # print(sheet.cell_value(5, 2))
    # booksheet = workbook.sheet_by_index(0)  # 用索引取第一个sheet
    # booksheet = workbook.sheet_by_name('Sheet1')  # 或用名称取sheet
    # 读单元格数据
    # cell_11 = booksheet.cell_value(0, 0)
    # cell_21 = booksheet.cell_value(1, 0)
    # 读一行数据
    row_3 = sheet.row_values(1)
    print(row_3)


def write(path):
    rb = xlrd.open_workbook(path)  # 打开weng.xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)  # 获取表单0
    ws.write(0, 0, 'changed!')  # 改变（0,0）的值
    ws.write(8, 0, label='好的')  # 增加（8,0）的值
    wb.save('weng.xls')


def openpyxl_write(path):
    workbook = openpyxl.load_workbook(path)
    worksheet = workbook.worksheets[0]
    # pool = Pool(5)
    pool = threadpool.ThreadPool(8)
    data =[]
    for row in list(worksheet.rows):
        data.append({'row0':row[0],'row1':row[1]})
    requests = threadpool.makeRequests(test, data)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # for index, row in enumerate(worksheet.rows):
    #     url = row[2].value
    #     if url == "二维码URL" :
    #         continue
        # g1 = gevent.spawn(test, index=index,url=url,row=row)
        # pool.apply_async(func=Foo, args=( index ,url,row[14]))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        # pool.apply_async(func=Foo, args=(url,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        # data_url = ""
        # try:
        #     data_url= get_ewm(url)
        # except BaseException as e:
        #     print  url
        # # worksheet.insert_cols(16)
        # # rows = list(worksheet.rows)
        # if index==0 :
        #     row[14].value = "URL"
        # else:
        #     row[14].value = data_url
        # if index ==5:
        #    break
    # pool.close()
    # pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    # pool.terminate()
    workbook.save(filename=path)
def test(row):
    print row
    url = row["row0"].value
    if url != "二维码URL":
        try:
            data_url= get_ewm(url)
            row["row1"].value = data_url
        except BaseException as e:
            print  url
# def Bar(arg):
    # print arg
# def Foo(i):
#     print i
# def Foo(index,url,row):
#     print  url
#     print  index
    data_url = ""
    # try:
    #     data_url = get_ewm(url)
    # except BaseException as e:
    #     print  url
    # if index == 0:
    #     row[14].value = "URL"
    # else:
    #     row[14].value = data_url

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
    openpyxl_write("./test.xlsx")
# red("./test.xlsx")
