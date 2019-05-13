# -*- coding: utf-8 -*-


# 同一段代码 在同一时间 只允许指定个进程访问，类似一个锁有多把钥匙
# ------------------------------------------->
import time
import random
from multiprocessing import Process, Semaphore


def ktv(i, sem):
    sem.acquire()  # 加锁
    print('%s走进ktv' % i)
    time.sleep(random.randint(1, 5))
    print('%s走出ktv' % i)
    sem.release()  # 释放锁


sem = Semaphore(4)
for i in range(20):
    p = Process(target=ktv, args=(i, sem))
    p.start()
# ------------------------------------------->
