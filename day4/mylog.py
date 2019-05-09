# -*- coding: utf-8 -*-


# Logger 记录器，暴露了应用程序代码能直接使用的接口。
# Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
# Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
# Formatter 格式化器，指明了最终输出中日志记录的布局。

# 创建方法: logger = logging.getLogger(logger_name)
#
# 创建Logger实例后，可以使用以下方法进行日志级别设置，增加处理器Handler。
#
# logger.setLevel(logging.ERROR) # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
# logger.addHandler(handler_name) # 为Logger实例增加一个处理器


# Handler 处理器
# Handler处理器类型有很多种，比较常用的有三个，StreamHandler，FileHandler
#
# 创建StreamHandler之后，可以通过使用以下方法设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter。
#
# ch.setLevel(logging.WARN) # 指定日志级别，低于WARN级别的日志将被忽略
# ch.setFormatter(formatter_name) # 设置一个格式化器formatter
# ch.addFilter(filter_name) # 增加一个过滤器，可以增加多个
# ch.removeFilter(filter_name) # 删除一个过滤器

# StreamHandler
# 创建方法: sh = logging.StreamHandler(stream=None)
#
# FileHandler
# 创建方法: fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)

# Formatter 格式化器
# 使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S。
#
# 创建方法: formatter = logging.Formatter(fmt=None, datefmt=None)
#
# 其中，fmt是消息的格式化字符串，datefmt是日期字符串。如果不指明fmt，将使用'%(message)s'。
# 如果不指明datefmt，将使用ISO8601日期格式。


import logging

# ----> create logger
logger_name = 'example'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# ----> create file handle
log_path = './log.log'
fh = logging.FileHandler(log_path, 'w', encoding='utf-8')
fh.setLevel(logging.WARNING)

# ----> create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# ----> add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)
