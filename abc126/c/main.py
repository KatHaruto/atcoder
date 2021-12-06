from math import ceil, log2

N, K = map(int, input().split())
s = 0.0
for i in range(1, N + 1):
    s += 0.5 ** ceil(log2(max(1, K / i)))
print(s / N)
