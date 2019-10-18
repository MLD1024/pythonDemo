import trip
# -*- coding: utf-8 -*-
import csv
import codecs
import trip
import json
import sys

reload(sys)
sys.setdefaultencoding("utf8")


@trip.coroutine
def jedegdata(filename='1.csv'):
    with codecs.open(filename=filename, mode='r', encoding='utf-8', errors="ignore") as f:
        reader = csv.reader(f)
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
            url = "http://10.144.100.205:8091/csb/1.0/QueryInvoice"
            r = yield trip.get(url, params=params)
            invoiceNo = json.loads(r.content)["resData"]["m:MsgResponse"]["Body"]["InvoiceList"]["Invoice"]["InvoiceNo"]
            if (data[4] != invoiceNo):
                with codecs.open(filename=r"data.csv", mode='a', encoding='utf-8') as f:
                    write = csv.writer(f, dialect='excel')
                    write.writerow(data)
            i = i + 1
@trip.coroutine
def main():
    r = yield trip.get('http://www.baidu.com/')
    print(r.content)


if __name__ == '__main__':
    # trip.run(main)
    trip.run(jedegdata)
