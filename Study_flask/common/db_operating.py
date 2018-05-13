#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/10 23:27
# 数据库增删改查,并转换成json格式

from sqlalchemy import create_engine
from Study_flask.base.connect2mysql import DB_URI

def db_select(SQL):
    engine = create_engine(DB_URI, echo=True)
    result = []
    try:
        with engine.connect() as con:
            rs = con.execute(SQL)
            for row in rs:
                result1 = {"id":row[0],
                           "name":row[1]
                           }
                result.append(result1)
    except Exception as e:
        return e
    # print(result)
    return result

# flask官网上的json转换例子
# def to_json(self):
#     return {
#         "id": self.id,
#         "title": self.title,
#         "order": self.order,
#         "completed": self.completed}
#
# def from_json(self, source):
#     if 'title' in source:
#         self.title = source['title']
#     if 'order' in source:
#         self.order = source['order']
#     if 'completed' in source:
#         self.completed = source['completed']
print(db_select("select * from flask_users"))

