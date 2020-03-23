import sys


def solve(n, m, data):
    d = [[0] * m for i in range(n)]
    p = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                d[i][j] = data[i][j]
                p[i][j] = 'R'
            elif i == 0:
                d[i][j] = d[i][j-1] + data[i][j]
                p[i][j] = 'R'
            elif j == 0:
                d[i][j] = d[i-1][j] + data[i][j]
                p[i][j] = 'D'
            elif d[i-1][j] > d[i][j-1]:
                d[i][j] = d[i - 1][j] + data[i][j]
                p[i][j] = 'D'
            else:
                d[i][j] = d[i][j - 1] + data[i][j]
                p[i][j] = 'R'
    map = {'D': (-1, 0), 'R': (0, -1)}
    i = n - 1
    j = m - 1
    path = []
    while i > 0 or j > 0:
        dir = p[i][j]
        path.append(dir)
        i += map[dir][0]
        j += map[dir][1]
    coins = d[n-1][m-1]
    path.reverse()
    return coins, path


lines = sys.stdin.readlines()
l1 = lines[0].split(' ')
n = int(l1[0])
m = int(l1[1])
data = []
for line in lines[1:]:
    data.append([int(x) for x in line.split(' ')])

coins, path = solve(n, m, data)

print(coins)
print(''.join(path))