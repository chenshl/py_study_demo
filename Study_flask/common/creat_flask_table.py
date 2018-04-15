#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/15 22:44
# 使用SQLAlchemy：要使用ORM来操作数据库，首先需要创建一个类来与对应的表进行映射

from sqlalchemy import Column,Integer,String
from Study_flask.base.connect2mysql import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URI,echo=True)

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class User(Base):
    # 定义表名为flask_users_new
    __tablename__ = 'flask_users_new'

    # 将id设置为主键，并且默认是自增长的
    id = Column(Integer,primary_key=True)
    # name字段，字符类型，最大的长度是50个字符
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(100))

    # Base.metadata.create_all()

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "<User(id='%s',name='%s',fullname='%s',password='%s')>" % (self.id,self.name,self.fullname,self.password)

# 执行创建表，使用我们一开始创建的那个引擎
Base.metadata.create_all(engine)

if __name__ == "__main__":
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    print(ed_user.name)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)
    session.commit()