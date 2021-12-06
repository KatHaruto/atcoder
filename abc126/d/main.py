N = int(input())
g = {}
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    if u not in g.keys():
        g[u] = []
    if v not in g.keys():
        g[v] = []

    g[u].append([v, w])
    g[v].append([u, w])

c = {1: 1}

visited = set()
queue = [1]
while queue:
    t = queue.pop(0)
    visited.add(t)
    for n, w in g[t]:
        if n not in visited:
            c[n] = c[t] if w % 2 == 0 else (c[t] + 1) % 2
            queue.append(n)
[print(c[i]) for i in range(1, N + 1)]
