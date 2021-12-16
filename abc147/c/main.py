from itertools import product

N = int(input())
p = []
for i in range(1, N + 1):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        p.append([i, x, y])
m = -1
for pro in product((False, True), repeat=N):
    for i, x, y in p:
        if not pro[i - 1]:
            continue

        if pro[x - 1] != y:
            break
    else:
        m = max(m, sum(pro))
print(m)
