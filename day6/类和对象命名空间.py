# -*- coding: utf-8 -*-

# class Course:
#     language='Chinese'
#     def __init__(self,teacher,name,price):
#         self.teacher=teacher
#         self.name=name
#         self.price=price
#
# python=Course('Brice','python',20000)
# Course.language
# python.language
# python.language = 'english'

# 当类变量为不可变数据类型时： 对象可以访问到类变量，但是没有修改权限，如果赋值修改则会给自身添加一个同名对象属性，但是类属性是不发生改变
# 一旦修改后，该对象就再也访问不到该类属性了。只有通过del来删除自身的这个属性后，才能访问
# del python.language

# 当类变量为可变数据类型： 对象可以共享类变量，对象对类变量重新赋值对类变量生效

# ----> 创建一个类，每实例化一个对象就记录下来 最终所有的对象共享这个数据

# class Foo:
#     count=0
#     def __init__(self):
#         print('对象:%s'%self)
#         Foo.count+=1
#
# a=Foo()
# b=Foo()
# print(a.count)
# print(b.count)
