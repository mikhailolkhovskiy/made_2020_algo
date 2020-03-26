import sys
import time
from random import (
    randint,
    seed,
)
from math import (
    log2,
)

seed(time.time())


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def is_prime(n):
    if n == 3 or n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    def check_not_prime(x, s, n):
        for j in range(s - 1):
            x = x * x % n
            if x == 1:
                return True
            if x == n - 1:
                return False
        return True

    r = max(int(log2(n)), 10)
    for i in range(r):
        s = 0
        t = n - 1
        while t % 2 == 0:
            s += 1
            t //= 2
        a = randint(2, n - 2)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        if check_not_prime(x, s, n):
            return False

    return True


def simple_factors(n, result):
    i = 2
    m = n
    while i * i <= m and n >= 1:
        if n % i == 0:
            n = n // i
            result.append(i)
        else:
            i += 1
    if n > 1:
        result.append(n)


def pollard_factors(n, result):
    def f(x):
        return (x * x + 1) % n

    a1 = randint(0, n)
    a2 = f(f(a1))
    while gcd(n, abs(a1 - a2)) == 1:
        a1 = f(a1)
        a2 = f(f(a2))
    d = gcd(n, abs(a1 - a2))
    factors(d, result)
    factors(n // d, result)


def factors(n, result):
    if is_prime(n):
        result.append(n)
    else:
        if n < 100:
            simple_factors(n, result)
        else:
            pollard_factors(n, result)
    result.sort()


lines = sys.stdin.readlines()
p = int(lines[0])

result = []
factors(p, result)
print(' '.join(map(str, result)))
