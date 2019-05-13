# -*- coding: utf-8 -*-

# ------------------------------------------->
# #----> 通过一个信号 来控制 多个进程 同时执行或者阻塞
# #事件  一个事件被创建后，默认是阻塞状态
#
# from multiprocessing import Event
#
# e=Event()   #创建一个事件对象
# print(e.is_set())  #查看事件的状态，默认阻塞
# e.set() # 将事件状态改为True以解除阻塞
# print(e.is_set())
#
# e.wait()   #是依据e.is_set()的值来决定是否阻塞 可以传参timeout
# print(12345)
# e.clear()  #将事件状态更改为False阻塞状态
# print(e.is_set())
# e.wait(5) #传入超时timeout参数，在阻塞状态下，触发超时后，结束阻塞
# print('*'*10)
#
# #----> set 和 clear  修改事件的状态True False
# #----> is_set 查看事件状态
# #----> wait 根据事件状态来决定自己是否阻塞  True不阻塞  阻塞超时timeout参数，阻塞超时后结束阻塞
# ------------------------------------------->

# 红绿灯事件
import time
import random
from multiprocessing import Process, Event


def light(e):
    while True:
        if not e.is_set():
            print('\033[31m红灯亮了\033[0m')
            time.sleep(5)
            e.set()
        else:
            print('\033[32m绿灯亮了\033[0m')
            time.sleep(3)
            e.clear()


def car(e, i):
    if not e.is_set():
        print('红灯----第%s辆车红灯等待中……' % i)
        e.wait()
        print('红灯等待时间到，第%s辆车通过' % i)
    else:
        print('绿灯----第%s辆车绿灯通过' % i)


e = Event()
traffic = Process(target=light, args=(e,))
traffic.start()

for i in range(20):
    cars = Process(target=car, args=(e, i))
    cars.start()
    time.sleep(random.random())
