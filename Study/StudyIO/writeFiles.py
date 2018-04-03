#!usr/bin/python
# -*- coding:utf-8 -*-
"""写文件"""
__author__ = "chensl"

import time

url2 = "C:/Users/Administrator/Desktop/pythontest2.txt"
with open(url2, "a") as file3:    # 打开方式为“a”，添加到原有数据后面
    file3.write("Hello, world!" + "\n")   # 写入后换行
    file3.write(time.asctime(time.localtime(time.time())) + "\n")

with open(url2, "r") as file4:
    for line in file4.readlines():
        print(line.strip())
