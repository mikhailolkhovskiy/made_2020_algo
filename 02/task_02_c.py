import sys
from collections import defaultdict


def solve(n, parents):
    graph = defaultdict(list)
    root = 0
    for i, p in enumerate(parents):
        graph[p-1].append(i)
        if p == 0:
            root = i

    dp0 = [0] * n
    dp1 = [0] * n

    def dfs(cur):
        s0 = 0
        s1 = 0
        for v in graph[cur]:
            dfs(v)
            s0 += max(dp0[v], dp1[v])
            s1 += dp0[v]

        dp0[cur] = s0
        dp1[cur] = s1 + 1

    dfs(root)
    return max(dp0[root], dp1[root])


lines = sys.stdin.readlines()
n = int(lines[0])
parents = [int(x) for x in lines[1:]]

k = solve(n, parents)

print(k)
