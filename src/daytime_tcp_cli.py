# -*- coding:utf-8 -*-
# 给时间服务器发送请求获取时间

import socket
import time

dest_ip = '129.6.15.28'
dest_port = 13
addr = (dest_ip, dest_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

sock.connect(addr)
sock.sendall('')

data = sock.recv(64)

print data
