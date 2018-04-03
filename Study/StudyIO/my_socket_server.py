#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
socket服务端代码
@author:chensl
"""

import socket, threading, time

def tcplink(scck, addr):
    print("Accept new connection from %s:%s " % addr)
    sock.send(b"Welcome!")
    while True:
        data = sock.recv(1024)
        time.sleep(2)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("Hello, %s!" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Connection from %s:%s closed." % addr)


# 首先，创建一个基于IPv4和TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听端口
s.bind(("127.0.0.1", 9998))
# 接下来调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print("Waiting for connection...")
# 接下来服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创结案新线程类处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

