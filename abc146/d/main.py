from collections import deque

N = int(input())
g = {}
for i in range(1, N + 1):
    g[i] = {}
mem = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    mem.append([a, b])
    g[a][b] = -1
    g[b][a] = -1

visited = [False] * (N + 1)
visited[1] = True

d = deque()
d.append([1, -1])
max_c = -1
while d:
    v, prev_c = d.popleft()
    c = 0

    for n in g[v].keys():
        if visited[n]:
            continue
        c = c + 1 if c + 1 != prev_c else c + 2
        if c == len(g[v]) + 1:
            c = 1
        visited[n] = True
        max_c = max(max_c, c)
        g[v][n] = c
        g[n][v] = c
        d.append([n, c])
print(max_c)
for a, b in mem:
    print(g[a][b])
