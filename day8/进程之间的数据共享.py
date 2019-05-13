# -*- coding: utf-8 -*-


# 进程之间的数据共享Manager 是进程不安全的，同管道一样，可以加锁来实现进程安全

from multiprocessing import Process, Manager


def func(dic):
    dic['count'] = 200
    print(dic)


m = Manager()
dic = m.dict({'count': 100})

p = Process(target=func, args=(dic,))
p.start()
p.join()
print('主进程:', dic)
