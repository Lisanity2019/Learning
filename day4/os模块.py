# -*- coding: utf-8 -*-

import os
print(os.getcwd()) #----> 获取当前工作目录
# print(os.chdir(r'/Users/liyao/Desktop/Learning')) #  改变当前脚本工作目录    mac无需转义，兼容win添加转义
# print(os.curdir)   #----> 返回当前目录 .
# print(os.pardir)   #----> 返回当前目录的父目录 ..
# os.makedirs('a/b') #----> 创建目录，可创建多层递归目录
# os.removedirs('a/b') #----> 若目录为空，则删除，并返回上一级目录，则也删除，以此类推
# os.mkdir('name') #----> 创建单级目录
# os.rmdir('name') #----> 删除单级空目录，若目录不为空则无法删除，报错
# print(os.listdir(os.getcwd())) #----> 列出指定目录下的所有文件和子目录，包含隐藏文件，并以列表返回
# os.remove() #---->  删除一个文件
# os.rename() #----> 重命名文件或目录
# print(os.stat('re模块.py')) #----> 获取文件或目录信息
# print(os.sep) #---->  输出当前系统分隔符 跨平台使用
# print(os.linesep) #---->输出当前系统的行终止符
# print(os.pathsep) #---->输出当前系统用于分割文件路径的字符串
# print(os.name) #----> 当前系统平台
# os.system('ls') #----> 运行shell命令，直接显示
# print(os.popen('ls').read()) #----> 运行shell命令，返回执行结果
# print(os.environ) #---->获取系统环境变量
# print(os.path.split(os.getcwd())) #---->将路径分割成目录和文件名，返回元组
# os.path.dirname('/Users/liyao/Desktop/Learning/day4/collections模块.py') #---->返回path的目录
# print(os.path.exists('/Users/liyao/Desktop/Learning/day4/collections模块.py'))  #---->如果路径存在，返回true，否则false
# print(os.path.isabs('/aa'))  #---->如果path是绝对路径，返回true,不判断path是否存在
# print(os.path.isfile('/Users/liyao/Desktop/Learning/day4/collections模块.py'))  #---->如果path是一个存在的文件，返回true
# print(os.path.isdir('/Users/liyao/Desktop/Learning/day4/'))  #---->如果path是一个存在的目录，则返回true
# print(os.path.join('name','tell')) #---->拼接路径
# print(os.path.getatime('/Users/liyao/Desktop/Learning/day4/collections模块.py')) #---->返回最后访问时间的时间戳
# print(os.path.getmtime('/Users/liyao/Desktop/Learning/day4/collections模块.py'))  #---->返回最后修改时间的时间戳
# print(os.path.getsize(os.getcwd())) #---->返回path的大小