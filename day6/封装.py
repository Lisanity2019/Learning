# -*- coding: utf-8 -*-

# ----> 封装：属性和方法都藏起来，不被外部访问 变量名或方法名左边添加双下划线
# 所有的私有属性或方法，不能被类外部访问

# class Person:
#     def __init__(self,name,passwold):
#         self.name=name
#         self.__passwold=passwold #----> 私有属性
#
#     def __get_pwd(self): #----> 私有方法
#         print(self.__dict__)
#         return self.__passwold  #----> 在类的内部使用私有属性，会自动带上 _类名 进行转换  _Person__passwold
#
# alex=Person('alex','ssss')
# print(alex._Person__passwold) #----> 可以特殊调用，一般不这么做
# print(alex._Person__get_pwd())

# property 方法伪装成属性
# ----> 内置装饰器函数 只在面向对象中使用

# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return  self.__name+'同学'
#     @name.setter                    #----> setter  getter  deleter--del关联
#     def name(self,newname):
#         self.__name=newname
# xiaowang=Person('小王')
# print(xiaowang.name)

class Goods:  # ----> 实现打折活动
    discount = 0.5

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.discount


apple = Goods('苹果', 5)
print(apple.price)
