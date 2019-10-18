# -*- coding: utf-8 -*-
import cv2
from pyzbar import pyzbar
import csv

found = set()
capture = cv2.VideoCapture(0)
PATH = "test.csv"


def run():
    while (1):
        ret, frame = capture.read()
        test = pyzbar.decode(frame)
        for tests in test:
            testdate = tests.data.decode('utf-8')  # 读取解析到的二维码信息
            print(testdate)  # 输出二维码信息
            if testdate not in found:  # 判断扫描到的信息是不是之前扫描到的
                with open(PATH, 'a+') as f:
                    csv_write = csv.writer(f)
                    date = [testdate]
                    csv_write.writerow(date)
                found.add(testdate)  # 把没有扫描到的二维码信息存放到found变量里
        cv2.imshow('Test', frame)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    run()