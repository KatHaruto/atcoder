from collections import Counter

N = int(input())
A = list(map(int, input().split()))
d = Counter(A)
for i in range(1, N + 1):
    print(d[i])
