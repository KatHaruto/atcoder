from itertools import combinations
from math import sqrt

N, D = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))
cnt = 0
for u, v in combinations(range(N), 2):
    if sqrt(sum(map(lambda x: abs(x[0] - x[1]) ** 2, zip(X[u], X[v])))).is_integer():
        cnt += 1
print(cnt)
