# -*- coding: utf-8 -*-
import pandas as pd
import csv
import codecs
import MySQLdb
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding("utf8")


def get_conn():
    db = MySQLdb.connect(host='172.16.50.146', port=4000, user='shtelecom_query',
                         passwd='c7K2TWGRW1hyMMccSZG6WUNy6sWoBj', db='telecom-wx')
    return db


def execute_all(cursor, sql, args):
    cursor.execute(sql, args)
    with codecs.open(filename=r"data.csv", mode='a', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        results = cursor.fetchall()
        for result in results:
            write.writerow(result)


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        i = 0
        sql = 'SELECT DISTINCT a.openid, a.deviceno, a.bpnum FROM dx_weixin_bind a INNER JOIN dx_weixin_event_subscribe b ON a.bpnum = %s AND a.openid = b.FromUserName'
        for item in reader:
            i = i + 1
            args = tuple(item)
            print i
            execute_all(cursor=cur, sql=sql, args=args)
        conn.commit()
        cur.close()
        conn.close()


def request(params):
    github_url = "http://10.144.100.205:8091/csb/1.0/QueryInvoice"
    r = requests.get(github_url, params=params)
    return json.loads(r.content)["resData"]["m:MsgResponse"]["Body"]["InvoiceList"]["Invoice"]["InvoiceNo"]


def jedegdata(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8', errors="ignore") as f:
        reader = csv.reader(f)
        head = next(reader)
        i = 0
        for item in reader:
            print i
            data = tuple(item)
            params = {
                "bpnum": data[3],
                "fromDate": data[7] + "-" + data[8],
                "toDate": data[7] + "-" + data[8],
                "status": "2",
            }
            invoiceNo = request(params)
            # if (data[4] != invoiceNo):
            #     with codecs.open(filename=r"data.csv", mode='a', encoding='utf-8') as f:
            #         write = csv.writer(f, dialect='excel')
            #         write.writerow(data)
            i = i + 1


if __name__ == '__main__':
    jedegdata('12.csv')
