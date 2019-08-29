import logging

# 简单装饰器
def use_logging(func):
    def wrapper():
        logging.warn(f"{func.__name__} is running")
        return func()  # 传入参数foo，则func()等于foo()
    return wrapper


def foo():
    print("I am foo")


# 装饰器use_logging(foo)返回函数对象wrapper
# 所以这条语句相当于foo=wrapper
foo = use_logging(foo)
foo()   # 相当于执行wrapper()