#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
python的re模块包含了所有正则表达式的功能
@author:chensl
"""
import re

class MyRe():

    def __init__(self, testStr, reStr):
        self.testStr = testStr
        self.reStr = reStr

    def doReTelephone(self, testStr, reStr):
        if re.match(reStr, testStr):
            print("OK")
        else:
            print("Erro")

if __name__ == "__main__":
    testStr = "023-1234567"
    reStr = r"\d{3}\-\d{8}"
    dotele = MyRe(testStr, reStr)
    dotele.doReTelephone(testStr, reStr)
