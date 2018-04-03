# -*- coding:utf-8 -*-
def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L
        L2 = L + [0]
        L = [L1[i] + L2[i] for i in range(len(L1))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 20:
        break