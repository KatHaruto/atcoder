N, K = map(int, input().split())
p = set([])
for k in range(K):
    d = int(input())
    for pp in list(map(int, input().split())):
        p.add(pp)
print(N - len(p))
