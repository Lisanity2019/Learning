# -*- coding: utf-8 -*-

# ---->  staticmethod 静态方法 ***
# ---->  classmethod  类方法   ****

# class Goods: #----> 实现打折活动 classmethod
#     __discount=0.5
#     def __init__(self,name,price):
#         self.__name=name
#         self.__price=price
#
#     @property
#     def price(self):
#         return self.__price*Goods.__discount
#
#     @classmethod #---->类方法默认参数cls 把一个方法 变成一个类中的方法，这个方法可以直接被类调用，不需要依托任何对象
#     def change_discount(cls,new_discount): #---->修改折扣
#         Goods.__discount=new_discount
#
# Goods.change_discount(0.2)
# apple=Goods('苹果',5)
# print(apple.price)


class Login:
    def __init__(self, name, password):
        self.name = name
        self.pwd = password

    def login(self): pass

    @staticmethod
    def get_user_pwd():
        user = input('username:')
        pwd = input('password:')
        Login(user, pwd)


Login.get_user_pwd()
# ----> 在完全面向对象中，如果一个函数 即和对象没有关系 也和类没有关系
# 就用staticmethod将这个函数变成一个静态方法 静态方法没有默认参数
