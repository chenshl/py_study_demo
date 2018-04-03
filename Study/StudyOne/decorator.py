#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"文档说明"
__author__ = "csl"

import time
import functools

# 一个完整的decorator应该使用functools.wraps将原始函数的__name__等熟悉赋值到warpper函数中
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print("call %s():" % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print("%s %s():" % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log("execute111")
# def now():
#     print(time.time())
#     print(time.asctime(time.localtime(time.time())))
#
# now()

def log(*args, **kw):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            func(*args, **kw)
            print("end call")
            # return func(*args, *kw)
        print("begin call")
        return wrapper
    print("1")
    return decorator

@log()
def now():
    print(time.asctime(time.localtime(time.time())))

now()
