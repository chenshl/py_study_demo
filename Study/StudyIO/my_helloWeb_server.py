#!usr/bin/python3
# -*- coding:utf-8 -*-
"""
server端，负责启动WSGI服务器
@author:chensl
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from Study.StudyIO.my_helloWeb import application

print("hello")
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server("", 8000, application)
print("Serving HTTP on port 8000 ...")
# 开始监听HTTP请求
httpd.serve_forever()
