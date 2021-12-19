from itertools import permutations

N, M = map(int, input().split())
ta = []
ao = {}
for i in range(1, N + 1):
    ao[i] = []
for i in range(M):
    a, b = map(int, input().split())
    ta.append([a, b])
for i in range(M):
    a, b = map(int, input().split())
    ao[a].append(b)
    ao[b].append(a)

for p in permutations(range(1, N + 1), N):
    for a, b in ta:
        if p[b - 1] not in ao[p[a - 1]]:
            break
    else:
        print("Yes")
        exit()
print("No")
