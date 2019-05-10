# -*- coding: utf-8 -*-


import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

while True:
    info = '来自客户端2的消息>>> ' + input('>>> ')
    sk.sendto(bytes(info, encoding='utf-8'), ip_port)
    ret, addr = sk.recvfrom(1024)
    print(ret.decode('utf-8'))
    if ret.decode('utf-8') == 'bye':
        break

sk.close()
