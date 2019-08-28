import logging

# 简单装饰器


def use_logging(func):
    def wrapper():
        logging.warn(f"{func.__name__} is running")
        return func()  # 传入参数foo，则func()等于foo()
    return wrapper


def foo():
    print("I am foo")


foo = use_logging(foo)
foo()
