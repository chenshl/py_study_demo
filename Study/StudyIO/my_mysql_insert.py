#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
pymysql用于python3连接mysql数据库
需求描述：向数据库my_testsql的user表中插入数据，要求user_ID为当前日期加上一个两位数的值
python提供了commit()和rollback()两个事务方法
@author:chensl
"""

import pymysql
import datetime, random

def set_user_ID():
    today = datetime.date.today()  # 获取当前时间
    date = str(today).split("-", 2)  # 去除时间格式“-”号
    user_date = ""
    IDone = user_date.join(date)  # join()方法直接将列表或数组变成字符串
    num = random.randint(0, 99)   # random.randint()生成一个随机数
    # print(type(num))
    user_ID = IDone + str(num)
    return user_ID

# print(set_user_ID())


dbc = pymysql.connect("localhost", "root", "111111", "my_testsql")
cursor = dbc.cursor()  # 创建一个数据库游标对象
sql = """INSERT INTO user(user_ID, user_name, age) VALUES ("%s", "JACK", 22)""" % set_user_ID()

try:
    cursor.execute(sql)  # 执行sql语句
    dbc.commit()  # 提交数据库执行
except:
    dbc.rollback()  # 如果执行错则任务回滚

dbc.close()  # 关闭数据库连接
