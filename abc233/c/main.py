from itertools import product
from functools import reduce

N, X = map(int, input().split())
l = []
for n in range(N):
    a, *ll = map(int, input().split())
    l.append(list(ll))
cnt = 0
for ll in product(*l):
    if reduce(lambda x, y: x * y, ll) == X:
        cnt += 1
print(cnt)
