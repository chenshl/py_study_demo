#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
pillow支持python3，用于python的图像处理
@author: chensl
"""

from PIL import Image, ImageFilter
# 打开一个jpg图像文件，注意是当前路径
im = Image.open("C:/Users/Administrator/Desktop/IMG_2474.JPG")
# 获得图像尺寸
w, h = im.size
print("Original image size: %s*%s" % (w, h))
# 缩放到50%
im.thumbnail((w//10, h//10))
print("Resize image to: %s*%s" % (w//2, h//2))
# 把缩放后的图像用jpg格式保持
im.save("C:/Users/Administrator/Desktop/thumbnail.jpg", "jpeg")

# 模糊处理
im1 = Image.open("C:/Users/Administrator/Desktop/thumbnail.jpg")
# 应用模糊滤镜
im2 = im1.filter(ImageFilter.BLUR)
im2 = im1.filter(ImageFilter.DETAIL)
im2.save("C:/Users/Administrator/Desktop/blur.jpg", "jpeg")

