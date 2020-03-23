# Дано много чисел. Требуется разложить их все на простые множители.
#
# Входные данные
# В первой строке задано число n (2 ≤ n ≤ 300000). В следующих n строках заданы числа ai (2 ≤ ai ≤ 106),
# которые нужно разложить на множители.
#
# Выходные данные
# Для каждого числа выведите в отдельной строке разложение на простые множители в порядке возрастания множителей.
import sys


def solve(n, nums):
    m = max(nums) + 1
    lp = [0] * m
    primes = []
    for i in range(2, m):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            ip = i * p
            if p > lp[i] or ip >= m:
                break
            lp[ip] = p

    for num in nums:
        factors = []
        while num > 1:
            factors.append(str(lp[num]))
            num = int(num / lp[num])
        print(' '.join(factors))


lines = sys.stdin.readlines()
n = int(lines[0])
nums = [int(x) for x in lines[1:]]

solve(n, nums)
