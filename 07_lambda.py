x = lambda a : a + 10
print(x(5))

y = lambda x, y : x * y
print(y(6, 7))


def my_func(n):
    return lambda a : a * n

my_doubler = my_func(2)
print(my_doubler(3))

my_tripler = my_func(3)
print(my_tripler(3))