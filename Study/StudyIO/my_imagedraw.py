#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
PILde的ImageDraw提供了一系列绘图方法，让我们可以直接绘图
@author: chensl
"""

from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 * 60
width = 60 * 4
heigh = 60
image = Image.new("RGB", (width, heigh), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype("Arial.ttf", 36)  # 需要有Arial.ttf这种字体
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(heigh):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save("C:/Users/Administrator/Desktop/code.jpg", "jpeg")


