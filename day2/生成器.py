# -*- coding: utf-8 -*-
__author__ = 'liyao'

#生成器
#生成器函数
#生成器表达式

  #生成器函数:执行之后会得到一个生成器对象作为返回值
# def generator():
#     print(1)
#     yield 'a'
#
# ret=generator()
# print(ret)
# print(ret.__next__())
# for i in ret:print(i)

#自定义字符串生成器
# def generator():
#     for i in range(1,6):
#         yield '自定义字符串'+str(i)
#
#
# ret=generator()
#
# for i in ret:
#     print(i)

#python3方法 yield from 从容器中取
# def generator():
#     a='abcd'
#     yield from a
#
# g=generator()
# for i in g:
#     print(i)

