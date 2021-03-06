# -*- coding: utf-8 -*-

# ----> 尽量在开头导入模块

# ----> import 模块名 执行该模块名
# 模块名.变量名 和本文件中的变量名完全不冲突
# ----> import 模块名 as 重命名的模块名：可以将多个模块重命名同一个名字，提高代码的兼容性

# ----> from 模块名 import 变量名
# 直接使用 变量名 就可以操作
# 如果本文件中有相同的变量名就会发生冲突
# ----> from 模块名 import 变量名1，变量名2
# ----> from 模块名 import *
# 将模块中的所有变量名都放入内存中
# 如果本文件中有相同变量名会冲突
# __all__ 模块如果没有这个变量，就会导入所有名字； 如果有，则只导入all这个列表中规定的变量名

# ----> __name__
# 在模块中 当直接执行这个模块的时候，__name__='__main__'  当在其他模块中引入这个模块的时候，__name__=='这个模块的名字'

# ----> 包：一大堆模块的集合
