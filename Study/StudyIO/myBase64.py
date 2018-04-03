#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
base64是一种用64个字符来表示任意二进制数据的方法
@author: chensl
"""
import base64

enStr = base64.b64encode(b"binary\x00string")
print(enStr)
deStr = base64.b64decode(enStr)
print(deStr)
print(type(str(enStr)))
