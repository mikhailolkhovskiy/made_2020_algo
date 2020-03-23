import sys


def solve(line):
    n = len(line)
    map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    dp = {}

    def search(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        if i > j:
            return 0, ""
        elif i == j:
            result = 1, ""
        else:
            min_d = n + 1
            if map.get(line[i]) == line[j]:
                d, s = search(i + 1, j - 1)
                min_d = d
                result = d, line[i] + s + line[j]
            for k in range(i, j):
                d1, s1 = search(i, k)
                d2, s2 = search(k + 1, j)
                if min_d > d1 + d2:
                    min_d = d1 + d2
                    result = d1 + d2, s1 + s2
        dp[(i, j)] = result
        return result

    return search(0, n - 1)[1]


lines = sys.stdin.readlines()

s = solve(lines[0].strip())

print(s)
