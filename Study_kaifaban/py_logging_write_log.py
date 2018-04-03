#!usr/bin/env/python
# coding=UTF-8
'''用logging模块封装一个同时输出在屏幕和文件的日志模块'''

import logging
from logging import handlers

# 1.生成日志对象
logger = logging.getLogger("web")  #创建日志logger对象
logger.setLevel(logging.DEBUG)  #设置全局日志级别，全局优先级大于handler对象的日志优先级，意思会先验证全局的日志级别

# 2、生成handler对象
ch = logging.StreamHandler()  #输出到屏幕
ch.setLevel(logging.WARNING)
# fh = logging.FileHandler("web.log")  #输出到文件
# fh = handlers.RotatingFileHandler("web.log",maxBytes=100,backupCount=3)  #handler指定文件大小后重新存储文件（按文件大小）
fh = handlers.TimedRotatingFileHandler("web.log",when="h",interval=24,backupCount=3)  #handler指定时间分日志文件，保存最近的3个上一个会被覆盖
fh.setLevel(logging.DEBUG)
# 2.1、把handler对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 3、生成formatter对象
ff = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
cf = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d")
# 3.1、绑定formatter对象
ch.setFormatter(cf)
fh.setFormatter(ff)


logger.info("你好！这里的日志开始输出了！")
logger.warning("warning!warning!")
logger.error("error,error!")
