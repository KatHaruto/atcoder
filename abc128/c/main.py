N, M = map(int, input().split())
k = []
s = []
for _ in range(M):
    kk, *ss = map(int, input().split())
    k.append(kk)
    s.append(set(ss))
p = list(map(int, input().split()))
res = 0
for i in range(2 ** N):
    light = set([])
    for j in range(N):
        if (i >> j) & 1:
            light.add(j + 1)
    for k, ss in enumerate(s):
        cnt = 0
        for l in ss:
            if l in light:
                cnt += 1
        if cnt % 2 != p[k]:
            break
    else:
        res += 1
print(res)
