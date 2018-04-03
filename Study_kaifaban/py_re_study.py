#!usr/bin/env/python
# coding=utf-8
'''用正则表达式模块拿到一个网页上的所有连接'''
#  '.' 匹配除\n（换行符）之外的任意一个字符
#  '^' 匹配字符开头，由开头开始匹配   '^' = '\A'
#  '$' 匹配字符结尾，由结尾开始匹配   '$' = '\Z'
#  '*' 匹配*前的字符0次或者多次
#  '+' 匹配前一个字符1次或多次
#  '?' 匹配前一个字符1次或0次
#  '{m}' 匹配前一个字符m次
#  '{m,n}' 匹配前一个字符m到n次
#  '|' 匹配条件or的关系，如：[a-z|A-Z]{2}
#  '(...)' 分组匹配，需要用groups()方法获取数据，如：([a-z]{2})([0-9]{11})
#  '\d' 匹配数字0-9  等于[0-9]
#  '\D' 匹配非数字
#  '\w' 匹配[A-Za-z0-9]
#  '\W' 匹配非[A-Za-z0-9]
#  '\s' 匹配空白字符、\t、\n、\r
#  '(?P<省>\d{3})(?P<市>[0-9]{3})' 分组匹配，并可以<>中键值对返回字典类型，groupdict()方法获取结果数据

import re
import requests

url = "http://www.tuozhen.com"
respons = requests.get(url)
print(respons.status_code)
# print(respons.text)
pattern = "[0-9]{11}"
# ree = re.findall(pattern, respons.text)
ree = re.search(pattern, respons.text)
if ree:
    # print(ree)
    print(ree.group())