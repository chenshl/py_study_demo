#!usr/bin/python
# coding=utf-8
'''基于python套接字的半双工通讯实现客户端同服务器的对话（对讲机）'''

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建socket对象
sock.bind(('',9001))  #创建服务器端口
print('this is server...,I am OK')
sock.listen(60)  #设置服务器最大监听数
con,add = sock.accept()
while True:
    recvs = con.recv(512).decode()  #设置最大接收数量
    print('接收到的数据为：%s' %recvs)
    if recvs == 'breack':
        break
    sends = input('请输入要发送的内容"breack"退出：')
    con.send(sends.encode())
    if sends == 'breack':
        break
sock.close()  #关闭socket对象
