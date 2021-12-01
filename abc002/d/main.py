def check(group):
    for p in group:
        for q in group:
            if q == p:
                continue
            if q not in d[p]:
                return -1
    return len(group)


N, M = map(int, input().split())
d = {}
for i in range(1, N + 1):
    d[i] = set([])

for i in range(M):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)
max_n = 1
for i in range(2 ** N):
    group = []
    for j in range(N):
        if (i >> j) & 1:
            group.append(j + 1)
    max_n = max(max_n, check(group))
print(max_n)
