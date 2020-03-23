import sys


def solve(n, prices):
    memo = {}

    def search(i, k,):
        if (i, k) in memo:
            return memo[(i, k)]
        else:
            if i == n:
                return 0, set()
            else:
                if prices[i] > 100:
                    price, days = search(i + 1, k + 1)
                    r = prices[i] + price
                else:
                    price, days = search(i + 1, k)
                    r = prices[i] + price
                if k > 0:
                    k_price, k_days = search(i + 1, k - 1)
                    if r > k_price:
                        r = k_price
                        days = k_days | {i}
                memo[(i, k)] = (r, days)
                return r, days

    price, days = search(0, 0)
    k2 = len(days)
    k = 0
    for i, p in enumerate(prices):
        if p > 100 and i not in days:
            k += 1
    k1 = k - k2
    k_days = [x + 1 for x in days]
    return price, k1, k2, sorted(k_days)


lines = sys.stdin.readlines()
n = int(lines[0])
prices = [int(x) for x in lines[1:]]

price, k1, k2, days = solve(n, prices)

print(price)
print('{} {}'.format(k1, k2))
for d in days:
    print(d)
