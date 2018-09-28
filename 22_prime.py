import time
import math

def is_prime_v1(n):
    """Return 'True' if 'n' is prime. False otherwise"""
    if n==1:
        return False

    for d in range(2, n):
        if n%d == 0:
            return False
    
    return True


for i in range (1, 21):
    print(i, is_prime_v1(i))



def is_prime_v2(n):
    """Return 'True' if 'n' is prime. False otherwise"""
    if n==1:
        return False

    for d in range(2, math.floor(math.sqrt(n))):
        if n%d == 0:
            return False
    
    return True


def is_prime_v3(n):
    """Return 'True' if 'n' is prime. False otherwise"""
    if n==1:
        return False

    if n == 2:
        return True

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    
    return True