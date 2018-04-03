#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""读写文件"""
__author__ = "chensl"

str1 = "C:/Users/Administrator/Desktop/pythontest1.txt"
try:
    file1 = open(str1, "rb")
    # print(file1.read())
    # print(file1.read(2))
    # print(file1.readline())
    print(file1.readlines())
    print("end!")
finally:
    if file1:
        file1.close()

# python引入了with语句来自动帮我们调用close()方法
with open(str1, "r", encoding="gbk", errors="ignore") as file2:  # 错误的编码格式直接忽略
    print(file2.read())
    print("end!")

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较方便
# 如果是配置文件，调用readlines()最方便
with open(str1, "rb") as file3:
    for lines in file3.readlines():
        print(lines.strip())  # 把末尾的“ln”删掉
    print("end!")
    
