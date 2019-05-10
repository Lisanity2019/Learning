# -*- coding: utf-8 -*-

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))  # 绑定要通讯的别人的IP端口

while True:
    info = input('client:>>> ')
    sk.send(bytes(info, encoding='utf-8'))

    ret = sk.recv(1024).decode('utf-8')
    print('server:>>> ', ret)
    if ret == 'bye':
        break

sk.close()
