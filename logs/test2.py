# -*- coding: utf-8 -*-
import os
import os.path


# rootdir = 'D:\loganalyze'
# list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
# for i in range(0 ,len(list)):
#     path = os.path.join(rootdir ,list[i])
#     if os.path.isfile(path):
#         print  path
#     else:
#         print path
#



def getFile(path):
    list = os.listdir(path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        filepath = os.path.join(path, list[i])
        if os.path.isfile(filepath):
            print  filepath
        else:
            getFile(filepath)




if __name__ == '__main__':
    getFile('D:\loganalyze')