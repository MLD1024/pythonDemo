# -*- coding: utf-8 -*-
import csv
import codecs
import requests
import json
import sys

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
            print i;
            data = tuple(item)
            params = {
                "bpnum": data[3],
                "fromDate": data[7]+"-" + data[8],
                "toDate": data[7]+"-" + data[8],
                "status": "2",
            }
            invoiceNo = request(params)
            if (data[4] != invoiceNo):
                with codecs.open(filename=r"data.csv", mode='a', encoding='utf-8') as f:
                    write = csv.writer(f, dialect='excel')
                    write.writerow(data)
            i = i + 1
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    jedegdata('1.csv')
