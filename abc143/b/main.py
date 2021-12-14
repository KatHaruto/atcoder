from itertools import combinations

N = int(input())
d = list(map(int, input().split()))

print(sum([u * v for u, v in combinations(d, 2)]))
