import logging


# 带参数的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn(f"{func.__name__} is running")
            elif level == "info":
                logging.info(f"{func.__name__} is running")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@use_logging(level="warn")
def foo(name):
    print(f"I am {name}")


foo('JackChen')