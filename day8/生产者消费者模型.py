# -*- coding: utf-8 -*-

# 进程队列Queue是进程安全的，队列中的值只能同一时间只能被一个进程访问
# 生产者消费者模型

# 生产者 进程
# 消费者 进程
# ------------------------------------------->
##用向队列添加None方式，解决消费者随生产者结束而结束，比较low
# import time
# import random
# from multiprocessing import Process,Queue
#
# def producer(name,food,q):
#     for i in range(5):
#         time.sleep(random.randint(1,2))
#         f='%s生产的%s%s'%(name,food,i)
#         print('%s生产了%s%s'%(name,food,i))
#         q.put(f)
#
# def consumer(name,q):
#     while True:
#         food=q.get()
#         if food is None:
#             print('%s获取到了空'%name)
#             break
#         print('\033[032m%s消费了%s\033[0m'%(name,food))
#         time.sleep(random.randint(1,2))
#
#
# q=Queue(20)
# p1=Process(target=producer,args=('Alex','包子',q))
# p2=Process(target=producer,args=('Eric','饺子',q))
# c1=Process(target=consumer,args=('Alice',q))
# c2=Process(target=consumer,args=('Bruce',q))
# p1.start()
# p2.start()
# c1.start()
# c2.start()
# p1.join()
# p2.join()
# q.put(None)
# q.put(None)
# ------------------------------------------->
import time
import random
from multiprocessing import Process, JoinableQueue


# 思路：将生产者进程设为同步join，并再生产者里代码段执行完毕后加入join()方法，所有生产的数据被全部处理完毕之前被 阻塞
# ----> 再将消费者设置为守护进程，当生产者结束后，消费者也结束，在消费者里处理完一个数据调用一次task_done()方法，
# 该方法类似一个计数器，当生产的所有数据都被消费者处理完毕后，生产者进程结束。生产者结束后，消费者由于加入了守护进程，
# 所以消费者进程也会结束。这一流程触发前提是消费者队列数据全部处理完毕

def producer(name, food, q):
    for i in range(5):
        time.sleep(random.randint(1, 2))
        f = '%s生产的%s%s' % (name, food, i)
        print('%s生产了%s%s' % (name, food, i))
        q.put(f)
    q.join()  # 阻塞 直到队列中的所有数据 全部被处理完毕


def consumer(name, q):
    while True:
        food = q.get()
        print('\033[032m%s消费了%s\033[0m' % (name, food))
        time.sleep(random.randint(1, 2))
        q.task_done()


q = JoinableQueue(20)
p1 = Process(target=producer, args=('Alex', '包子', q))
p2 = Process(target=producer, args=('Eric', '饺子', q))
c1 = Process(target=consumer, args=('Alice', q))
c2 = Process(target=consumer, args=('Bruce', q))
p1.start()
p2.start()
c1.daemon = True  # 设置为守护进程之后，主进程中的代码执行完毕之后，子进程自动结束
c2.daemon = True  # 设置守护进程必须在启动进程之前，否则会引发异常
c1.start()
c2.start()
p1.join()
p2.join()
