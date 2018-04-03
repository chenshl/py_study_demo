import requests
import json

r = requests.get("http://httpbin.org/get?name='akui'&email='a_kui@163.con'")
print(r.text)                #以文本形式输出response对象
r1 = json.loads(r.text)      #将response对象的json格式文本转换为Python的字典数据类型
print(r1)
print("您的IP地址为：%s" % (r1["origin"]))