# -*- coding: utf-8 -*-
import pandas as pd
import csv
import codecs
import MySQLdb
import requests
import json
import sys


def get_conn():
    db = MySQLdb.connect(host='172.16.50.146', port=4000, user='shtelecom_query',passwd='c7K2TWGRW1hyMMccSZG6WUNy6sWoBj', db='telecom-wx')
    return db


def execute_all(cursor, sql, args):
    cursor.execute(sql, args)
    with codecs.open(filename=r"./data1.csv", mode='a', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        results = cursor.fetchall()
        for result in results:
            write.writerow(result)


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        conn = get_conn()
        cur = conn.cursor()
        i = 0
        # sql = 'SELECT DISTINCT a.openid, a.deviceno, a.bpnum FROM dx_weixin_bind a INNER JOIN dx_weixin_event_subscribe b ON a.bpnum = %s AND a.openid = b.FromUserName'
        sql = 'SELECT  a.scene, a.scantime  FROM dx_weixin_scene a where a.openid = %s '
        for item in reader:
            i = i + 1
            # args = tuple(item[0].strip())
            args = item[0].strip()
            print i
            execute_all(cursor=cur, sql=sql, args=args)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    read_csv_to_mysql('./data.csv')
