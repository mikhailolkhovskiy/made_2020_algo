import heapq as hq


def solve(n, k, data):
    d = [0] * (len(data) + 2)
    p = [0] * (len(data) + 2)
    data = [0] + data + [0]
    last_k = [(0, 0)]

    def max_prev(i):
        while last_k[0][1] < i - k:
            hq.heappop(last_k)
        return -last_k[0][0], last_k[0][1]

    for i in range(1, len(d)):
        v, idx = max_prev(i)
        d[i] = v + data[i]
        p[i] = idx
        hq.heappush(last_k, (-d[i], i))
    coins = d[i]
    steps = [i + 1]
    while i > 0:
        steps.append(p[i] + 1)
        i = p[i]
    return coins, len(steps)-1, reversed(steps)


with open('input.txt', 'rt') as f:
    l1 = f.readline().split(' ')
    n = int(l1[0])
    k = int(l1[1])
    if n > 2:
        l2 = f.readline().split(' ')
        data = [int(x) for x in l2]
    else:
        data = []


coins, n_steps, steps = solve(n, k, data)

with open('output.txt', 'wt') as f:
    f.write(str(coins) + '\n')
    f.write(str(n_steps) + '\n')
    f.write(' '.join(map(str, steps)))
