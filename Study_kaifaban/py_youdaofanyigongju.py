#!usr/bin/python
# _*_ coding: UTF-8 _*_
# @author : csl
# @date   : 2018/03/03 17:04
'''通过有道翻译做一个翻译工具，类似爬虫概论获取数据'''
#好像有道翻译post请求里面加了加密sign签名串，不能直接访问成功

import urllib.request
import urllib.parse
import json

def request2youdao_post(url,indata):
    #url:访问地址
    #parmas:访问参数
    parmas = {}
    parmas["i"] = indata
    parmas["from"] = "AUTO"
    parmas["to"] = "AUTO"
    parmas["smartresult"] = "dict"
    parmas["client"] = "fanyideskweb"
    parmas["salt"] = "1520060880760"
    parmas["sign"] = "be6b2575720856ad97dd308025a75e53"
    parmas["doctype"] = "json"
    parmas["version"] = "2.1"
    parmas["keyfrom"] = "fanyi.web"
    parmas["action"] = "FY_BY_REALTIME"
    parmas["typoResult"] = "false"
    parmas = urllib.parse.urlencode(parmas).encode("utf-8")  #转换为urllib可识别的格式
    response = urllib.request.urlopen(url,parmas)
    html = response.read().decode("utf-8")
    target = json.loads(html)  #将json格式转换成Python格式
    # print(target)


#输入要翻译的内容
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
print("请输入要翻译的内容：")
indata = input()
request2youdao_post(url,indata)

