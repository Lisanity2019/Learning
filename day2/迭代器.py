# -*- coding: utf-8 -*-
__author__ = 'liyao'

# 对象只要含有__iter__方法，都是可迭代的 ---->可迭代协议---->内部含有__next__和__iter__方法的就是迭代器

list = [1, 2, 3]
# print(dir(list)) #传入类型所支持调用的方法

# print(list)

# print(dir(list))
# print(dir(list.__iter__()))
# print(set(dir(list.__iter__())) - set(dir(list)))

#
# iterator=list.__iter__()
# print(iterator.__next__())

# 判断是否可迭代和迭代器
from collections import Iterable, Iterator

# print(isinstance([], Iterator))
# print(isinstance([], Iterable))

#自建数据类型迭代器
# class A:
#     def __iter__(self): pass
#
#     # def __next__(self): pass
#
# a = A()
# print(isinstance(a, Iterable))
# print(isinstance(a, Iterator))


# dict={1:"hhh",2:"dddd"}
# for key in dict:print(key,dict[key])
# for item in dict.items():print(item)

#迭代器的好处：
#从容器类型中一个一个取值
#节省内存空间：迭代器会随着每次循环__next__生成一个，而不是一次性生成
# print(range(3)) #打印迭代器range(0, 3)，不会直接生成数

