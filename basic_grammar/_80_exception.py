# 异常处理

# 非法的算术会导致异常
number = 1 / 0

# try-except-else-finally 语句可以捕获异常，
# try 块中的代码为需要进行异常处理的代码
# except 为需要拦截的异常以及对该异常的处理代码
# else 块中的代码为没有发生异常时需要执行的代码
# finally 块中的代码无论是否发生异常都会执行
try:
    number = 1 / 0
except ZeroDivisionError:
    # pass表示占位符，表示该处没有代码需要执行
    pass
    print("除数不能为0")
else:
    print("没有发生异常")
finally:
    print("无论是否发生异常都会执行")


