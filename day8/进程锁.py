# -*- coding: utf-8 -*-

# ----> 买票问题(不加锁)
# ------------------------------------------->
import json
import time
from multiprocessing import Process, Lock


# def show(i):
#     with open('ticket.json') as f:
#         dic=json.load(f)
#     print('余票：%s'%dic['ticket'])
#
# def buy_ticket(i):
#     with open('ticket.json') as f:
#         dic=json.load(f)
#         time.sleep(0.1)
#     if dic['ticket']>0:
#         dic['ticket']-=1
#         time.sleep(0.1)
#         with open('ticket.json','w') as f:
#             json.dump(dic,f)
#         print('\033[32m用户%s买到票了\033[0m'%i)
#     else:
#         print('\033[31m用户%s没买到！\033[0m'%)
#
# for i in range(10):
#     p=Process(target=show,args=(i,))
#     p.start()
#
# for i in range(10):
#     p2=Process(target=buy_ticket,args=(i,))
#     p2.start()

# ------------------------------------------->
# 加锁
def show(i):
    with open('ticket.json') as f:
        dic = json.load(f)
    print('余票：%s' % dic['ticket'])


def buy_ticket(i, lock):
    lock.acquire()  # 上锁，禁止其它进程访问下面的代码，阻塞其它进程
    with open('ticket.json') as f:
        dic = json.load(f)
        time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        time.sleep(0.1)
        with open('ticket.json', 'w') as f:
            json.dump(dic, f)
        print('\033[32m用户%s买到票了\033[0m' % i)
    else:
        print('\033[31m用户%s没买到！\033[0m' % i)
    lock.release()  # 释放锁


for i in range(10):
    p = Process(target=show, args=(i,))
    p.start()

lock = Lock()  # 实例化锁

for i in range(10):
    p2 = Process(target=buy_ticket, args=(i, lock))
    p2.start()

# ------------------------------------------->
