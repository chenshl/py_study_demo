#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/03/28 21:27
# 提供可以被调用的接口

import requests

class api(object):

    def __init__(self, server, parma):
        self.server = server
        self.parma = parma

    def send(self):
        # print("你传入的接口名称是:%s；你传入的参数是:%s" %(self.server, self.parma))
        result_data = {"result":"1", "code":"200", "messege":"你好，你post方式访问 %s 成功了！" %self.server}
        return result_data


class api_next(object):

    def __init__(self, server, parma):
        self.server = server
        self.parma = parma

    def send(self):
        result_data = {"result":"1", "code":"200", "messege":"你好，你get方式访问 %s 成功了！" %self.server}
        return result_data


class douban_api(object):

    def __init__(self, host, request_methord="get", parma=None):
        self.host = host
        self.request_methord = request_methord
        self.parma = parma

    def send(self):
        if self.request_methord == "get":
            url = self.host + "?" + self.parma
            requests.packages.urllib3.disable_warnings()  # 关闭HTTPS错误警告
            req = requests.get(url, verify=False)  # 关闭SSL验证
            # print(req.status_code)
            # print(req.text)
            return [req.status_code, req.text]
        else:
            rstr = "请求方法错误，该接口只支持get方法。。。"
            return rstr


class baifubao_api(object):

    def __init__(self, host, request_methord="get", parma=None):
        self.host = host
        self.request_methord = request_methord
        self.parma = parma

    def send(self):
        if self.request_methord == "get":
            url = self.host + "?" + self.parma
            requests.packages.urllib3.disable_warnings()
            req = requests.get(url, verify=False)
            return [req.status_code, req.text]
        else:
            rstr = "请求方法错误，该接口只支持get方法。。。"
            return rstr



if __name__ == "__main__":
    host = "https://api.douban.com/v2/book/search"
    parma = 'q="百年孤独"'
    # host = "https://www.baifubao.com/callback"
    # parma = "cmd=1059&callback=phone&phone=15823777272"

    req1 = douban_api(host,"get", parma).send()
    # reql = baifubao_api(host, "get", parma).send()
    print(req1)
    print(req1[1].strip("'"))



