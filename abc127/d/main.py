N, M = map(int, input().split())
a = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]
BC.sort(key=lambda x: x[1], reverse=True)
a.sort()
i = 0
for j in range(len(BC)):

    if i >= N:
        break
    while i < N and BC[j][0] > 0 and a[i] < BC[j][1]:
        a[i] = BC[j][1]
        BC[j][0] -= 1
        i += 1
print(sum(a))
