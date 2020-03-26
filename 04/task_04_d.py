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

    r = 10
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


def solve(nums):
    for num in nums:
        if is_prime(num):
            print('YES')
        else:
            print('NO')


lines = sys.stdin.readlines()
n = int(lines[0])
nums = [int(x) for x in lines[1:n + 1]]
solve(nums)
