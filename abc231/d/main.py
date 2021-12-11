N, M = map(int, input().split())
if M == 0:
    print("Yes")
    exit()
d = {}
for i in range(1, N + 1):
    d[i] = set([])
for i in range(M):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)
    if len(d[a]) > 2 or len(d[b]) > 2:
        print("No")
        exit()

seen = [False] * (N + 1)


def dfs(d, s):
    seen[s] = True
    stack = [[s, -1]]
    while stack:
        v, pre_v = stack.pop(-1)
        for ne in d[v]:
            if ne == pre_v:
                continue
            if seen[ne]:
                print("No")
                exit()
            seen[ne] = True
            stack.append([ne, v])


for a in d.keys():
    if not seen[a]:
        dfs(d, a)
print("Yes")
