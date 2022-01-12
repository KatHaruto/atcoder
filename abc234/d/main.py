N, K = map(int, input().split())
P = list(map(int, input().split()))
l = []
ll = set([])
m = N - K + 1
for i in range(N - 1, K - 2, -1):
    l.append(m)
    ll.add(P[i])
    if P[i] >= m:
        m -= 1
    while m in ll:
        m -= 1
print(*l[::-1], sep="\n")
