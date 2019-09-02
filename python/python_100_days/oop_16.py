import logging


def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn(f"{func.__name__} is running")
        return func(*args, **kwargs)  # 传入参数foo，则func()等于foo()
    return wrapper


@use_logging
def foo(name, age, height):
    print(f"I am {name}, age {age}, height {height}")


foo('JackChen', 43, height=176)