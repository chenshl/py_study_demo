# -*- coding:utf-8 -*-
import requests
import json

name = input("请输入你的姓名：")
email = input("请输入你的邮箱：")
data = {"name": name, "email": email}
url = "http://httpbin.org/post"
req = requests.post(url=url, data=data)
req.encoding = "utf-8"
sc = req.status_code
print(req.encoding)
print(req.text)
print("响应状态码：%s" % (sc))
# print(json.loads(req.text))
