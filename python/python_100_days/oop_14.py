import logging


def use_logging(func):
    def wrapper():
        logging.warn(f"{func.__name__} is running")
        return func()  # 传入参数foo，则func()等于foo()
    return wrapper


def log(func):
    def wrapper():
        print("log is running")
        return func()
    return wrapper

@use_logging
@log
def foo():
    print("I am foo")


foo()
