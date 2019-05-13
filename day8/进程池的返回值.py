# -*- coding: utf-8 -*-

# 进程池特有，子进程可以有返回值,Process创建进程方式不支持返回值

import time
from multiprocessing import Pool


def func(i):
    time.sleep(0.5)
    return i * i


# ------------------------------------------->
# p=Pool()
# res_l=[]
#
# for i in range(10):
#     res=p.apply_async(func,args=(i,))
#     res_l.append(res)
#
# for v in res_l:print(v.get())
# ------------------------------------------->
p = Pool()
ret = p.map(func, range(10))  # 自带join同步
print(ret)
