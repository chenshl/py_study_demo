#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/15 22:20
# 通过SQLAlchemy连接数据库

from sqlalchemy import create_engine

#  数据库的配置变量
#  username是连接数据库的用户名，password是连接数据库的密码，host是连接数据库的域名，port是数据库监听的端口号，database是连接哪个数据库的名字
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_testsql'
USERNAME = 'root'
PASSWORD = '111111'
# 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# # 创建数据库引擎
# engine = create_engine(DB_URI)
#
# # 创建连接
# with engine.connect() as con:
#     rs = con.execute("SELECT 1")
#     print(rs.fetchone())
