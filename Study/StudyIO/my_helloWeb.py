#!/user/bin/python
# -*- coding:utf-8 -*-
"""
实现WEB应用程序的WSGI处理函数
@author:chensl
"""

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>Hello, web!<h1>"]
