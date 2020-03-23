import sys


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def is_prime(n):
    return False


def simple_factors(n):
    result = []
    i = 2
    m = n
    while i * i<= m and n != 1:
        if n % i == 0:
            n = n // i
            result.append(i)
        else:
            i += 1
    result.append(n)
    return result


def pollard_factors(n):
    return []


def factors(n):
    if is_prime(n):
        return [n]
    else:
        if n < 100:
            return simple_factors(n)
        else:
            return pollard_factors(n)


lines = sys.stdin.readlines()
p = int(lines[0])

print(factors(p))

