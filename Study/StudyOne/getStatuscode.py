# -*- coding:utf-8 -*-
import requests

url = input("请输入你要发送HTTP请求的URL连接：")
try:
    res = requests.get(url)
    code = res.status_code
    # text = res.text
    print(code)
    # print(text)
except Exception:
    print("你输入的HTTP请求地址：%s 出现连接异常，请确认地址是否正确！" % (url))
