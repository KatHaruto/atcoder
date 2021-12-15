from itertools import permutations
from math import sqrt
from math import factorial

N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))
s = 0
for n in permutations(range(N)):
    for i in range(N - 1):
        s += sqrt(
            (xy[n[i + 1]][0] - xy[n[i]][0]) ** 2 + (xy[n[i + 1]][1] - xy[n[i]][1]) ** 2
        )
print(s / factorial(N))
