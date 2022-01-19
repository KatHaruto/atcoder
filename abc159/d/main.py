from functools import reduce
from collections import Counter


def cmb(n, r):
    numerator = reduce(lambda x, y: x * y, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y, [k + 1 for k in range(r)])
    return int(numerator / denominator)


N = int(input())
A = list(map(int, input().split()))
C = dict(Counter(A))
ans = 0
for k, v in C.items():
    if v < 2:
        continue
    ans += cmb(v, 2)
for a in A:
    print(ans - cmb(C[a], 2) + cmb(C[a] - 1, 2))
