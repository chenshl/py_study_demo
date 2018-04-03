# -*- coding:utf-8 -*-
import time
import datetime

localtime = time.localtime(time.time())
print(localtime)
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1 = count()
print(f1)

print(datetime.datetime.now())