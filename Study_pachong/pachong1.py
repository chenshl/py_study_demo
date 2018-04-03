# -*- coding:UTF-8 -*-
import urllib.request
# urllib返回的是HTTPResponse类型数据，requestes返回的是json类型数据

# url = "http://www.douban.com/"
url = "http://www.tuozhen.com"
webHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  # 伪装成浏览器
req = urllib.request.Request(url, headers=webHeader)     # 用Request()方法封装请求数据，data=可以发送post请求
webPage = urllib.request.urlopen(req) # 获取页面数据
data = webPage.read()
data = data.decode("utf-8")           # decode()方法进行解码
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
print(data)
