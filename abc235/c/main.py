N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = {}
cnt = {}
for i, a in enumerate(A):
    if a not in d.keys():
        d[a] = {1: i}
        cnt[a] = 1
    else:
        d[a][cnt[a] + 1] = i
        cnt[a] += 1
for _ in range(Q):
    x, k = map(int, input().split())
    if x not in d.keys() or k not in d[x].keys():
        print(-1)
    else:
        print(d[x][k] + 1)
