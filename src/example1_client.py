# -*- coding:utf-8 -*-

import socket
import time

dest_ip = '172.93.35.211'
dest_port = 8080
addr = (dest_ip, dest_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

sock.connect(addr)
sock.sendall(b'hello ... \n\n')

data = sock.recv(64)

print(data)