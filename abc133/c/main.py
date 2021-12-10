from itertools import combinations

L, R = map(int, input().split())
p = 2019
n = R // p - L // p + (L % p == 0)
m = 2019
if n >= 1:
    print(0)
else:
    for u, v in combinations(range(L, R + 1), 2):
        m = min(m, (u % p) * (v % p) % p)
    print(m)
