# Решите в целых числах систему уравнений
#
# {x≡a(modn)x≡b(modm),
# где n и m взаимно просты. Среди решений следует выбрать наименьшее неотрицательное число.
#
# Входные данные
# Первая строка входных данных содержит число N, 1≤N≤104, — количество тестов, для которых нужно решить задачу.
#
# Следующие N строк содержат по четыре целых числа ai, bi, ni и mi (1≤ni,mi≤109, 0≤ai<ni, 0≤bi<mi).
#
# Выходные данные
# Для каждого из тестов выведите искомое наименьшее неотрицательное число xi.
import sys


def ex_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = ex_gcd(b % a, a)
    return gcd, y - (b // a) * x, x


def solve(params):
    for a1, a2, m1, m2 in params:
        g, q, p = ex_gcd(m2, m1)
        x1 = q * m2
        g, q, p = ex_gcd(m1, m2)
        x2 = q * m1
        x = (a1 * x1 + a2 * x2) % (m1 * m2)
        print(x)


lines = sys.stdin.readlines()
n = int(lines[0])
data = []
for line in lines[1:]:
    data.append([int(x) for x in line.split(' ')])

solve(data)

