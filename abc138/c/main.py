from functools import reduce

N = int(input())
v = list(map(int, input().split()))
v = sorted(v)
print(reduce(lambda x, y: (x + y) / 2, v))
