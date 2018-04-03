#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
安装mysql-connector驱动连接MySQL数据库
@author:chensl
"""

import pymysql

# 打开数据库
dbc = pymysql.connect("localhost", "root", "111111", "my_testsql")
# 使用cursor()方法创建一个游标对象cursor
cursor = dbc.cursor()
# 使用execute()方法执行sql查询
cursor.execute("SELECT VERSION()")
# 使用fetchone()方法获取单条数据
data = cursor.fetchone()
print("Database version : %s" % data)
# 关闭数据库连接
dbc.close()
