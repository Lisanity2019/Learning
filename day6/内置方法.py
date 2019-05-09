# -*- coding: utf-8 -*-

# ----> __str__ __repr__  __del__
# from math import pi
# class A:
#     def __str__(self):
#         return '%.2f'%pi
#     # pass
#     def __del__(self):  #----> 析构函数
#         print('执行我啦')
#
#     def __call__(self, *args, **kwargs):
#         print('aaaa')
# a=A()
# a()   # 对象()  就是执行__call__
# print(str(a)) #----> 打印一个对象的时候，就是调用__str__
#
# del a  #----> __del__

# __getitem__  __setitem__  __delitem__ 属性的增删改查

# class B:
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self, item):
#         if hasattr(self,item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# b=B('bob')
# print(b['name'])
# b['name']='alex'
# print(b['name'])
# del b['name']
# print(b['name'])
