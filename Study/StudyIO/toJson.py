#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
json模块提供了非常完善的python对象到json格式的转换
author:chensl
"""

import json

d = dict(name="Bob", age="23", score=88)
print(json.dumps(d))
print(type(d))

json_str = '{"age":20, "score":88, "name":"Bob"}'
print(json.loads(json_str))
print(type(json.loads(json_str)))
print(type(json_str))
