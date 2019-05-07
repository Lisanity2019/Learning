# -*- coding: utf-8 -*-

# try:
#     ret=int(input('number >>>'))
#     print(ret*'*')
# except ValueError: #----> except 只能处理对应的错误类型，支持多分支
#     print('输入错误!')

try:
    ret = int(input('number >>>'))
    print(ret * '*')

except Exception as e:  # ----> Exception 万能异常捕获，万能异常处理放在已知捕获错误类型的最后面
    print('你错了，老铁^_^', e)

else:
    print('------------')  # ----> 如果没有错误，try代码段执行顺利的时候，执行

finally:
    print('finally')  # ---->不管有没有异常，执行
