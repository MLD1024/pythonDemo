# -*- coding: utf-8 -*-
import os
import os.path
import re
import pandas as pd
from pandas import DataFrame
import xlsxwriter

rule1 = "(/wechat.*)\?"
rule2 = "/wechat.*"
regex1 = re.compile(rule1, re.IGNORECASE)
regex2 = re.compile(rule2, re.IGNORECASE)
keys = {}


# /wechat/Rest/BillPay/item?payid=2019101315709414103451206228
# /wechat/Rest/BillPay/item?payid=2019101315709414103451206228
def get_key(line):
    if (line.find("?") > 0):
        regex = regex1
        m = regex.search(line)
        if m:
            return m.group(1)
        return '!NotMatch!'
    else:
        regex = regex2
        m = regex.search(line)
        if m:
            return m.group(0)
        return '!NotMatch!'

def counter_key(key):
    keys.setdefault(key, 0)
    keys[key] += 1


def getFile(path):
    list = os.listdir(path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        filepath = os.path.join(path, list[i])
        if os.path.isfile(filepath):
            # 这是程序的入口
            print  filepath
            with open(filepath) as f:
                for line in f:
                    # 一行一行处理日志信息
                    key = get_key(line)  # 获取路径
                    counter_key(key)  # 统计次数
        else:
            getFile(filepath)


def save(path):
    data = pd.read_excel(path)
    url = []
    count = []
    for (key, value) in keys.items():
        url.append(key)
        count.append(value)
    data['URL'] = url
    data['COUNT'] = count
    DataFrame(data).to_excel(path, index=False, header=True)


if __name__ == '__main__':
    getFile('D:\loganalyze')
    save("./data.xlsx")
