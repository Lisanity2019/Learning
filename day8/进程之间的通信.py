# -*- coding: utf-8 -*-


# 进程之间的通信 IPC
# ------------------------------------------->
# #----> 队列 是进程安全的
# import time
# from multiprocessing import Queue
#
# q=Queue(3)
# q.put(1)
# q.put(2)
# print('队列是否已满:',q.full())
# q.put(3)
# print('队列是否已满:',q.full())
# print(q.get())
# print(q.get())
# print(q.get())
# print('队列是否已空:',q.empty())
# # print(q.get(timeout=2)) get()传入timeout参数可以在指定时间后返回结果，队列为空，超时取值报错，不用一直阻塞等待队列有值
#
# #循环 隔一段时间get()取值
# while True:
#     try:
#         q.get_nowait() #队列为空，调用该方法会报错，可用异常捕获，好处：如果队列为空，可以不用等待
#     except:
#         print('队列已空')
#         time.sleep(1)

# ------------------------------------------->
# 进程间的通信
def produce(q):
    q.put('hello')


def consume(q):
    print(q.get())


from multiprocessing import Process, Queue

q = Queue()
p = Process(target=produce, args=(q,))
c = Process(target=consume, args=(q,))
p.start()
c.start()
# ------------------------------------------->
# 通过队列作为中介，来实现子进程之间的消息传递
