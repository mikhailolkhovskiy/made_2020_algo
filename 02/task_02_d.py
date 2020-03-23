import sys


def get_bit(mask, i):
    return (mask >> i) & 1


def solve(n, graph):
    m = 2**n
    dp = []
    p = []
    max_v = 10**7 * n
    for i in range(n):
        dp.append([max_v] * m)
        p.append([(0, 0)] * m)
        dp[i][0] = 0

    for mask in range(1, m):
        for i in range(n):
            if not get_bit(mask, i):
                for j in range(n):
                    if get_bit(mask, j):
                        p_m = mask - (1 << j)
                        new_v = dp[j][p_m] + graph[j][i]
                        if new_v <= dp[i][mask]:
                            dp[i][mask] = new_v
                            p[i][mask] = (j, p_m)

    min_w = max_v
    min_i = 0
    for i in range(n):
        v = dp[i][m-1 - (1 << i)]
        if min_w > v:
            min_w = v
            min_i = i

    path = [min_i + 1]
    i, mask = min_i, m-1 - (1 << min_i)

    while mask > 0:
        i, mask = p[i][mask]
        path.append(i + 1)
    return min_w, path


lines = sys.stdin.readlines()
n = int(lines[0])
graph = []
for line in lines[1:]:
    graph.append([int(x) for x in line.split(' ')])

length, path = solve(n, graph)

print(length)
print(' '.join(map(str, path)))
