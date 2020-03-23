import sys


def solve(n, m, field):
    dp = []
    max_mask = 2**n
    for i in range(n * m + 1):
        dp.append([0] * max_mask)
    dp[0][0] = 1

    for j in range(m):
        for i in range(n):
            x = n * j + i
            for mask in range(max_mask):
                v = dp[x][mask]
                if mask & 1 == 1 or field[i][j] == 'X':
                    dp[x + 1][mask >> 1] += dp[x][mask]
                else:
                    if j < m - 1 and field[i][j + 1] != 'X':
                        dp[x + 1][(mask >> 1) + 2**(n - 1)] += dp[x][mask]
                    if i < n - 1 and field[i + 1][j] != 'X' and mask & 2 == 0:
                        dp[x + 1][(mask >> 1) + 1] += dp[x][mask]

    return dp[n * m][0]


lines = sys.stdin.readlines()
line = lines[0].split(' ')
n, m = int(line[0]), int(line[1])
field = [x.strip() for x in lines[1:]]
k = solve(n, m, field)
print(k)
