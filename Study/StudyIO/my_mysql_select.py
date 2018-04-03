#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
数据库表查询
fetchone()该方法获取下一个查询结果集，结果集是一个对象
fetchall()接收全部的返回结果行
rowcount()这是一个只读属性，并返回执行execute()方法后影响的行数
@author:chensl
"""

import pymysql

dbc = pymysql.connect("localhost", "root", "111111", "my_testsql")
cursor = dbc.cursor()
sql = """SELECT * FROM user WHERE age >= %s""" % 20
try:
    cursor.execute(sql)
    results = cursor.fetchall()  # 获取所有记录列表
    print(results)
    for row in results:
        id = row[0]
        user_ID = row[1]
        user_name = row[2]
        age = row[3]
        print("id = %s, user_ID = %s, user_name = %s, age = %s" %
              (id, user_ID, user_name, age))
except:
    print("Error: unable to fetch data")

dbc.close()

