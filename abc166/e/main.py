from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = 0
for j in range(N):
    ans += d[j - A[j]]
    d[j + A[j]] += 1
print(ans)
