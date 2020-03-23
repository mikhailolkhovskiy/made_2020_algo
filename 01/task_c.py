import sys


def solve(n, data):
    d = [0] * n
    p = [-1] * n
    max_seq = 1
    max_seq_end = 0
    for i in range(n):
        max_d = 0
        for j in range(i):
            if data[i] > data[j]:
                if max_d < d[j]:
                    max_d = d[j]
                    p[i] = j
        d[i] = max_d + 1
        if max_seq < d[i]:
            max_seq = d[i]
            max_seq_end = i
    seq = []
    i = max_seq_end
    while i >= 0:
        seq.append(data[i])
        i = p[i]
    seq.reverse()
    return max_seq, seq


lines = sys.stdin.readlines()
n = int(lines[0])
data = [int(x) for x in lines[1].split(' ')]

k, seq = solve(n, data)

print(k)
print(' '.join(map(str, seq)))
