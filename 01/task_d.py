import sys


def solve(str1, str2):
    memo = {}

    def search(s1, i1, s2, i2):
        if (i1, i2) in memo:
            return memo[(i1, i2)]
        if len(s1) == i1 or len(s2) == i2:
            result = max(len(s1) - i1, len(s2) - i2)
        else:
            if s1[i1] == s2[i2]:
                result = search(s1, i1 + 1, s2, i2 + 1)
            else:
                result = 1 + min(search(s1, i1 + 1, s2, i2 + 1),
                                 search(s1, i1, s2, i2 + 1),
                                 search(s1, i1 + 1, s2, i2))
        memo[(i1, i2)] = result
        return result

    return search(str1, 0, str2, 0)


lines = sys.stdin.readlines()
k = solve(lines[0].strip(), lines[1].strip())
print(k)
