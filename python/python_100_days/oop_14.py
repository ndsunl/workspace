import logging

<<<<<<< HEAD
# 简单装饰器
=======

>>>>>>> d2d93b96c4f0dca96bce889592589969757c8876
def use_logging(func):
    def wrapper():
        logging.warn(f"{func.__name__} is running")
        return func()  # 传入参数foo，则func()等于foo()
    return wrapper

<<<<<<< HEAD
# @语法糖
@ use_logging
=======

def log(func):
    def wrapper():
        print("log is running")
        return func()
    return wrapper

@use_logging
@log
>>>>>>> d2d93b96c4f0dca96bce889592589969757c8876
def foo():
    print("I am foo")


<<<<<<< HEAD
foo()
=======
foo()
>>>>>>> d2d93b96c4f0dca96bce889592589969757c8876
