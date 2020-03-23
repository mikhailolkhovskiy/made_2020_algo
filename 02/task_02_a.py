import sys

def get_bit(mask, i):
    return (mask >> i) & 1


def solve(n, rel):
    m = 2**n
    dp = [0] * m
    for mask in range(1, m):
        for i in range(n):
            if get_bit(mask, i):
                dp[mask] = max(dp[mask], dp[mask - (1 << i)])
                for j in range(n):
                    if get_bit(mask, j) and rel[i][j] == 'Y':
                        dp[mask] = max(dp[mask], dp[mask - (1 << i) - (1 << j)] + 1)
    return dp[m - 1] * 2


lines = sys.stdin.readlines()
n = int(lines[0])
rel = [x.strip() for x in lines[1:]]

k = solve(n, rel)

print(k)
