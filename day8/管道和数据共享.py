# -*- coding: utf-8 -*-

# 管道(双向通信) 在不同进程里仍然可以通信，但是是进程不安全的，可以通过加锁解决
# 队列 是基于 管道 + 锁 实现的

from multiprocessing import Process, Pipe, Lock

# ------------------------------------------->
# def func(conn):
#     while True:
#         msg=conn1.recv()
#         if msg is None:break
#         print(msg)
#
#
# conn1,conn2=Pipe()
#
# Process(target=func,args=(conn1,)).start()
# [conn2.send('数据%s'%i) for i in range(10)]
# conn2.send(None)
# ------------------------------------------->

# 用管道实现生产者消费者模型
import time
import random


def producer(con, pro, name, food):
    con.close()
    for i in range(5):
        time.sleep(random.random())
        f = '\033[031m%s生产的%s%s\033[0m' % (name, food, i)
        pro.send(f)
        print('\033[032m%s生产了%s%s\033[0m' % (name, food, i))
    pro.close()


def consumer(con, pro, lock, name):
    pro.close()
    while True:
        try:
            lock.acquire()
            msg = con.recv()
            lock.release()
            print('%s消费了 %s' % (name, msg))
            time.sleep(random.random())
        except EOFError:  # 用在捕获的异常里，关闭管道，并break跳出循环
            lock.release()
            con.close()
            break


con, pro = Pipe()
lock = Lock()
p = Process(target=producer, args=(con, pro, 'Alex', '包子')).start()
c1 = Process(target=consumer, args=(con, pro, lock, 'Bruce')).start()
c2 = Process(target=consumer, args=(con, pro, lock, 'Eric')).start()  # 多个消费者在同一个管道里访问数据，
# 会引发数据混乱，是不安全的，可以加锁解决
con.close()
pro.close()
