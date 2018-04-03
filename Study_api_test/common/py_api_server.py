#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28 21:27
# 提供可以被调用的接口

class testapi(object):

    def __init__(self, server, parma):
        self.server = server
        self.parma = parma

    def send(self):
        # print("你传入的接口名称是:%s；你传入的参数是:%s" %(self.server, self.parma))
        result_data = {"result":"1", "code":"200", "messege":"你好，你post方式访问 %s 成功了！" %self.server}
        return result_data


class testapi_next(object):

    def __init__(self, server, parma):
        self.server = server
        self.parma = parma

    def send(self):
        result_data = {"result":"1", "code":"200", "messege":"你好，你get方式访问 %s 成功了！" %self.server}
        return result_data

