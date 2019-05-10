# -*- coding: utf-8 -*-

# ----> socket(套接字) 套接字家族使用最广泛的是 AF_INET

import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ----> 避免服务重启的时候address already in use
sk.bind(('127.0.0.1', 8080))  # 绑定IP端口
sk.listen()  # 监听
conn, addr = sk.accept()  # 获取到一个客户端链接，已经完成三次握手建立一个链接 阻塞

while True:

    ret = conn.recv(1024).decode('utf-8')  # 接收到一个客户端发来的消息  阻塞
    print('client:>>> ', ret)
    if ret == 'bye':
        conn.send(bytes(ret, encoding='utf-8'))
        print('server:>>> ', ret)
        break
    info = input('server:>>> ')
    conn.send(bytes(info, encoding='utf-8'))

conn.close()  # 关闭与客户端的链接
sk.close()  # 关闭socket对象
