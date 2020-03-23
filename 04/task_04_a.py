import sys


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def primitive_root(params):
    pr = 0

    return pr


lines = sys.stdin.readlines()
p = int(lines[0])

print(primitive_root(p))

