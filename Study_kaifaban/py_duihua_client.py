#!usr/bin/python
# coding=utf-8
'''基于python套接字的半双工通讯实现客户端同服务器的对话（对讲机）'''

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('this is client1...')
sock.connect(('127.0.0.1',9001))  #连接服务器
while True:
    sends = input('输入要发送的内容"breack"退出)：')
    sock.send(sends.encode())
    if sends == 'breack':
        break
    recvs = sock.recv(512).decode()  #设置最大接收数据
    print('接收到的数据为:%s' %recvs)
    if recvs == 'breack':
        break
sock.close()