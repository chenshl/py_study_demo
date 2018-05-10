#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/05/10 23:27
# 数据库增删改查,并转换成json格式

from sqlalchemy import create_engine
from Study_flask.base.connect2mysql import DB_URI

def db_select():
    engine = create_engine(DB_URI, echo=True)
    with engine.connect() as con:
        rs = con.execute("select * from flask_users")
        for row in rs:
            print(row)

db_select()
