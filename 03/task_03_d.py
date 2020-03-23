# Своим уравнением Ax + By + C = 0 задана прямая на плоскости. Требуется найти любую принадлежащую этой прямой точку,
# координаты которой — целые числа от  - 5·1018 до 5·1018 включительно, или выяснить что таких точек нет.
#
# Входные данные
# В первой строке содержатся три целых числа A, B и C ( - 2·109 ≤ A, B, C ≤ 2·109) — соответствующие коэффициенты
# уравнения прямой. Гарантируется, что A2 + B2 > 0.
#
# Выходные данные
# Если искомая точка существует, выведите ее координаты, иначе выведите единственное число -1.
import sys


def ex_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = ex_gcd(b % a, a)
    return gcd, y - (b // a) * x, x


def solve(a, b, c):
    g, x, y = ex_gcd(a, b)
    if c % g == 0:
        k = c // g
        return -x * k, -y * k
    else:
        return -1, ''


lines = sys.stdin.readlines()
a, b, c = [int(x) for x in lines[0].split(' ')]

x, y = solve(a, b, c)
print(x, y)