#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/15 22:36
# 用SQLAlchemy执行原生SQL

from sqlalchemy import create_engine
from Study_flask.base.connect2mysql import DB_URI

# 连接数据库
engine = create_engine(DB_URI, echo=True)

# 使用with语句连接数据库，如果发生异常会被捕获
with engine.connect() as con:
    # 先删除users表
    con.execute('drop table if exists flask_users')
    # 创建一个users表，有自增长的id和name
    con.execute('create table flask_users(id int primary key auto_increment,''name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into flask_users(name) values("xiaoming")')
    con.execute('insert into flask_users(name) values("xiaotuo")')
    # 执行查询操作
    rs = con.execute('select * from flask_users')
    # 从查找的结果中遍历
    for row in rs:
        print (row)
