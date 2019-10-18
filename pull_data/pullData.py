# -*- coding: utf-8 -*-
import pandas as pd
import csv
import codecs
import MySQLdb
import requests
import json
import sys
import pandas as pd
from pandas import DataFrame
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import os


# 获取连接
def get_conn():
    db = MySQLdb.connect(host='172.16.50.146', port=4000, user='shtelecom_query',
                         passwd='c7K2TWGRW1hyMMccSZG6WUNy6sWoBj', db='telecom-wx')
    return db


# 拉取数据
def pull(path):
    #  sql 语句
    sql = 'SELECT  a.scene, a.scantime  FROM dx_weixin_scene a where a.openid = %s'
    conn = get_conn()
    cur = conn.cursor()
    #  读取文件
    data = pd.read_excel(path, encoding="utf-8")
    openids = data["openid"]
    scene = []
    scantime = []
    i = 0
    for openid in openids:
        print i
        i = i + 1
        mysql_data = execute_all(cur, sql,openid)[0]
        scene.append(mysql_data[0])
        scantime.append(mysql_data[1])
    #  写入文件
    data['scene'] = scene
    data['scantime'] = scantime
    DataFrame(data).to_excel(path, index=False, header=True)


# 执行sql语句
def execute_all(cursor, sql, args):
    cursor.execute(sql, args)
    return cursor.fetchall()



if __name__ == '__main__':
    pull('./data.xlsx')
