def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 50):
#     print(n, ":", fibonacci(n))

# Implementing memoization
fibonacci_cache = {}
def fibonacci2(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        val = 1
    elif n == 2:
        val = 1
    elif n > 2:
        val = fibonacci2(n-1) + fibonacci2(n-2)

    # cache the value and return it
    fibonacci_cache[n] = val
    return val

for n in range(1, 101):
    print(n, ":", fibonacci2(n))


from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci3(n):
    # Check that the input is positive intefer
    if type != int or n < 1:
        return

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci3(n-1) + fibonacci3(n-2)

for n in range(1, 501):
    print(n, ":", fibonacci3('n'))