from collections import defaultdict
from re import L


N, M = map(int, input().split())
H = list(map(int, input().split()))
d = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    d[a - 1].add(b - 1)
    d[b - 1].add(a - 1)
ans = 0
for i in range(N):
    if len(d[i]) == 0:
        ans += 1
        continue
    if H[i] > max([H[e] for e in d[i]]):
        ans += 1
print(ans)
