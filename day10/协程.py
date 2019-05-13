# -*- coding: utf-8 -*-

# 协程： greenlet 真正的协程模块就是使用greenlet完成的切换
# 协程的意义:在遇到IO操作的时候，使用协程任务切换执行其他任务可以提高CPU利用率
# 进程+线程+协程

# 本质上是个线程
# 协程中任务的切换开销要远远小于进程线程之间的切换

# ------------------------------------------->
# import time
# def consumer():
#     while True:
#         x=yield
#         print('处理了数据:',x)
#
# def producer():
#     c=consumer()
#     next(c)
#     for i in range(10):
#         print('生产了数据:',i)
#         c.send(i)
#
# producer()
# ------------------------------------------->
# from greenlet import greenlet
#
#
# def eat():
#     print('eating start...')
#     g2.switch()
#     print('eating end')
#     g2.switch()
# def play():
#     print('playing start...')
#     g1.switch()
#     print('playing end')
#
# g1=greenlet(eat) #注册函数
# g2=greenlet(play)
# g1.switch()  #切换任务 切换后执行上一次切换前的位置继续执行
# ------------------------------------------->
from gevent import monkey;

monkey.patch_all()  # 将这行之后的导入的模块的IO阻塞打包
import gevent
import time
import threading


def eat():
    time.sleep(1)
    print(threading.currentThread().getName())  # 虚拟线程名 Dummy 虚假的
    print('eating start...')
    time.sleep(2)
    print('eating end')
    return '返回值'


def play():
    print(threading.currentThread().getName())
    print('playing start...')
    time.sleep(0.5)
    print('playing end')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
# gevent.joinall([g1,g2])
g1.join()
g2.join()  # 该方法用于启动需要协程的任务，等待结束。
print(g1.value)  # 可以拿到执行函数的返回值
print('主线程')
# ------------------------------------------->
# 只有遇到协程模块能识别的IO操作的时候，程序才会进行任务切换
