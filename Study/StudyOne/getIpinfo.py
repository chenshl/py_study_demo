# -*- coding:utf-8 -*-
import requests
import json

url1 = "http://ip.taobao.com/service/getIpInfo.php"
ip1 = input("请输入你要查询的IP地址:")
ip2 = {"ip": ip1}       # 将IP转换成字典数据类型通过params传递给requestes.get()
req = requests.get(url=url1, params=ip2)
dict3 = req.text
print(req.text)
# dict1 = json.loads(req.text)       # json.load()方法和requests自带的.json()都可以将json转成Python数据
# print(dict1)
# print(dict1["data"]["area"])       # 在返回的字典内部嵌套了字典，所以要在对应键的值里面再对应的键
dict2 = req.json()                   # requests.json(）只能转换response为json的数据格式
print("你输入的IP地址所在的国家：%s" % (dict2["data"]["country"]))
print("你输入的IP地址所在的地区：%s" % (dict2["data"]["area"]))
print("你输入的IP地址所在的地区：%s" % (dict2["data"]["region"]))
print("你输入的IP地址所在的地区：%s" % (dict2["data"]["city"]))
