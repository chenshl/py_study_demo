# -*- coding:utf-8 -*-
import json

name = input("请输入您的姓名：")
phone = input("请输入您的电话号码：")
dict1 = {"name": name, "phone": phone}
json1 = json.dumps(dict1, ensure_ascii=False, indent=4)
print(json1)