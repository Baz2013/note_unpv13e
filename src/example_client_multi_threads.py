# -*- coding:utf-8 -*-
# 多线程的socket客户端

import threading
import socket
import time

MAX_THREAD = 10
HOST = '172.93.35.211'
PORT = 8080

def to_bytes(s):
    if bytes != str:
        if type(s) == str:
            return s.encode('utf-8')
    return s

class Client(threading.Thread):
    def __init__(self, name, host, port, msg):
        threading.Thread.__init__(self, name=name)
        self._name = name
        self._host = host
        self._port = port
        self._msg = msg
        self._addr = (self._host, self._port)

    def run(self):
        # time.sleep(0.01)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self._addr)
        send_msg = to_bytes(self._name) + b'|' + to_bytes(self._msg)  + b'\n\n'
        sock.sendall(send_msg)

        recv_data = sock.recv(64)
        print(to_bytes(self._name) + b'---->' + recv_data)

        sock.close()

def main():
    thread_lst = []
    for i in range(MAX_THREAD):
        t_name = 'thread' + str(i)
        thread = Client(t_name, HOST, PORT, 'hi, I am thread ' + str(i))
        thread.start()
        thread_lst.append(thread)

    for t in thread_lst:
        t.join(timeout=2)


if __name__ == '__main__':
    main()





