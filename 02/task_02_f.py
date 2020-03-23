import sys


def solve(n, nums):

    if nums[0] > nums[-1]:
        return -1, []

    def can_cut(i, k, j):
        return nums[i] > nums[k] < nums[j] or nums[i] < nums[k] > nums[j]

    cuts_memo = {}
    memo = {}

    def cut(i, j):
        if (i, j) in cuts_memo:
            return cuts_memo[(i, j)]
        if i + 1 == j:
            return []
        result = None
        for k in range(i + 1, j):
            if can_cut(i, k, j):
                cuts1 = cut(i, k)
                if cuts1 is None:
                    continue
                cuts2 = cut(k, j)
                if cuts2 is None:
                    continue
                result = cuts1 + cuts2 + [k]
                break

        cuts_memo[(i, j)] = result
        return result

    def search(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        min_cut = n + 1
        for k in range(i + 1, j):
            if nums[i] <= nums[k] <= nums[j]:
                c1, cuts1 = search(i, k)
                c2, cuts2 = search(k, j)
                if c1 + c2 < min_cut:
                    min_cut = c1 + c2
                    result = c1 + c2, cuts1 + cuts2
        if min_cut == n + 1:
            cuts = cut(i, j)
            if cuts is None:
                result = n + 1, None
            else:
                result = len(cuts), cuts
        memo[(i, j)] = result
        return result

    c, cuts = search(0, n - 1)
    if c == n + 1:
        return -1, []
    else:
        return c, [x + 1 for x in cuts]


lines = sys.stdin.readlines()
n = int(lines[0])
nums = [int(x) for x in lines[1].strip().split(' ')]

m, cuts = solve(n, nums)

print(m)
for c in cuts:
    print(c)
