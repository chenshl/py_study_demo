#!uer/bin/env python3
# -*- coding:utf-8 -*-
"""
sturct检查任意文件是否是位图文件，如果是打印出图片大小和颜色数
@author: chensl
"""

import os, struct

def bmpinfo(thepath):
    if os.path.isfile(thepath):
        with open(thepath, "rb") as f:
            bThirty = f.read(30)
            if len(bThirty) < 30:
                print("Not a bmp file!")
                return
            infos = struct.unpack("<ccIIIIIIHH", bThirty)
            if infos[0] != b"B" or infos[1] != b"M":
                print("Not a bmp file!")
                return
            print("The bmp file is %s * %s,and colors are %s" % (infos[6], infos[7], infos[9]))
    else:
        print("File not exists!")


if __name__ == "__main__":
    print("Please input a bmp file's path:")
    p = input()
    bmpinfo(p)
