from functools import wraps


# 装饰器
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
    return x + x * x


f(2)
