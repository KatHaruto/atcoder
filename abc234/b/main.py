from itertools import combinations
from math import sqrt

N = int(input())
xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])
m = -1
for c1, c2 in combinations(xy, 2):
    m = max(m, sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2))
print(m)
