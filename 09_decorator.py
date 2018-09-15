
def check(checking_divide):
    def check_divide(a, b):
        if b == 0:
            print("Can't divide by zero.")
            return
        return checking_divide(a, b)
    return check_divide

@check
def divide(a, b):
    return a/b

print(divide(5, 3))

print("=======")

def outer(func):
    def wrapper(a, b):
        if b == 0:
            return "Can't divide by zero"
        return func(a, b)
    return wrapper

def divide(a, b):
    return a/b

divide = outer(divide)
print(divide(5, 0))


print("=======")
from functools import wraps

def my_logger(orig_func):
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='09_{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


@my_logger
def divide2(a, b):
    return a/b
print(divide2(5, 2))


print("=======")

def my_timmer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
    return wrapper


import time

@my_timmer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with ({}, {})'.format(name, age))

display_info("Vaijyant", 25)