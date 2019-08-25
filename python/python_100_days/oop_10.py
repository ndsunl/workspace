import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}()")
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper

@log
def test(p):
    print(test.__name__ + "param:" +p)

test("I'm a param")
