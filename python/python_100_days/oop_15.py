import logging


def use_logging(func):
    def wrapper(name):
        logging.warn(f"{func.__name__} is running")
        return func(name)  # 传入参数foo，则func()等于foo()
    return wrapper


@use_logging
def foo(name):
    print(f"I am {name}")


foo('Sunny')