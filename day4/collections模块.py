# -*- coding: utf-8 -*-

#collections模块 #---->  扩展数据类型
#内置基本数据类型(6个)： 列表  元组  字典  集合  数字  字符串
#----> 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
#----> 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）


#----------------------------->具名元组

#---->因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，
#---->所以在这里引入了 collections.namedtuple 这个工厂函数，来构造一个带字段名的元组。具名元组的实例和普通元组消耗的内存一样多，
#---->因为字段名都被存在对应的类里面。

from collections import namedtuple  #----------------------------->具名元组
# Point=namedtuple('point','x y')
# # Point=namedtuple('point',['x','y']) #---->有两种方法定义
# p=Point(1,2)
# print(p)


#----> 类属性 _fields：包含这个类所有字段名的元组
#----> 类方法 _make(iterable)：接受一个可迭代对象来生产这个类的实例
#----> 实例方法 _asdict()：把具名元组以 collections.OrdereDict 的形式返回，可以利用它来把元组里的信息友好的展示出来

# #----> 定义一个namedtuple类型User，并包含name，sex和age属性
# User=namedtuple('User','name sex age')
# #----> 创建一个User对象
# user=User('liyao','male',26)
# #----> 获取所有字段名
# print(user._fields)
# #----> 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
# user=User._make(['liyao','male',26])
# print(user)
# #----> 获取用户的属性
# print(user.name)
# print(user.sex)
# print(user.age)
# #----> 修改对象属性，注意要使用"_replace"方法
# user=user._replace(age=27)
# print(user)
# #----> 将User对象转换成字典，注意要使用"_asdict"
# print(user._asdict())

#----------------------------->具名元组

#----------------------------->队列
# Queue 的种类：
# FIFO： Queue.Queue(maxsize=0)  LIFO: 即 Last in First Out, 后进先出,与栈的类似
# FIFO 即 First in First Out, 先进先出。Queue 提供了一个基本的 FIFO 容器，使用方法很简单, maxsize 是个整数，
# 指明了队列中能存放的数据个数的上限。一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。如果 maxsize 小于或者等于 0，队列大小没有限制。

# 基本方法：
#
# 　　 Queue.Queue(maxsize=0)   FIFO， 如果 maxsize 小于 1 就表示队列长度无限
#        Queue.LifoQueue(maxsize=0)   LIFO， 如果 maxsize 小于 1 就表示队列长度无限
#        Queue.qsize()   返回当前队列的大小
#        Queue.empty()   如果队列为空，返回 True, 反之 False
#        Queue.full()   如果队列满了，返回 True, 反之 False
#        Queue.get([block[, timeout]])   读队列，timeout 等待时间，如果在timeout时间内没有取到就退出
#        Queue.put(item, [block[, timeout]])   写队列，timeout 等待时间
#
import queue
# q=queue.Queue(2)
# q.put(10)
# q.put(5)
#
# print(q.get())
# # print(q.get())
#
# print(q.qsize())
# print(q.empty())
# print(q.full())


