#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
前端调用my_socket_server，先打开my_socket_server.py服务端
@author:chensl
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("127.0.0.1", 9998))
# 接收欢迎消息
print(s.recv(1024).decode("utf-8"))
for data in [b"Michael", b"Tracy", b"Sarah"]:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode("utf-8"))
s.send(b"exit")
s.close()
