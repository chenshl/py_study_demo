#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
hashlib提供了常见的摘要算法，如md5,sha1等等
摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
@author: chensl
"""

import hashlib

# Python内置MD5加密
md5 = hashlib.md5()
# md5.update("how to use md5 in python hashlib?".encode("utf-8"))
md5.update("111111".encode("utf-8"))
print(md5.hexdigest())

