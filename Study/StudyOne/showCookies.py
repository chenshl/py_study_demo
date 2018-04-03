# -*- coding:utf-8 -*-
import requests
import json

str1 = input("请输入一组cookie，格式为key=value，直接回车表示输入结束")
list1 = str1.split(" ", str1.count(" "))       #将输入的字符串转换为列表格式
print(list1)

# 用循环的方式自动添加为字典类型的数据输入
cookies = {}
ck = {}
for i in range(len(list1)):
    str2 = list1[i]
    list2 = str2.split("=", str2.count("="))
    # print(list2)
    cookies = {list2[0]: list2[1]}
    ck.update(cookies)
print(ck)
# req = requests.get("http://httpbin.org/cookies", cookies=ck)
# req = requests.get("http://httpbin.org/cookies/set?name=aaa", cookies=ck)
req = requests.get("http://httpbin.org/cookies/delete?name=aaa", cookies=ck)
print(req.text)
