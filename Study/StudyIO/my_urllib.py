#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
urllib的request模块可以非常方便的抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回http响应
@author: chensl
"""

from urllib import request, parse

with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", data.decode("utf-8"))


# 模拟浏览器发送GET请求
print("********\n")
req = request.Request("http://www.douban.com")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as r:
    print("Status:", r.status, r.reason)
    for k, v in r.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", r.read().decode("utf-8"))


# 模拟发送post请求
print("**********\n")
print("Login to weibo.cn...")
email = input("Email:")
passwd = input("Password:")
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req1 = request.Request("https://passport.weibo.cn/sso/login")
req1.add_header("Origin", "https://passport.weibo.cn")
req1.add_header("User-Agent", "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
req1.add_header("Referer", "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F")

with request.urlopen(req1, data=login_data.encode("utf-8")) as f1:
    print("Status:", f1.status, f1.reason)
    for k, v in f1.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", f1.read().decode("utf-8"))