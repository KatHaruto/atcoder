import sys

sys.setrecursionlimit(1000001)

N, Q = map(int, input().split())

graph = {}
counter = {}
for i in range(1, N + 1):
    graph[i] = []
    counter[i] = 0
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p] += x
seen = [False] * (N + 1)


def dfs(g, s, x, cnt):
    if cnt == N:
        return
    seen[s] = True
    for n in g[s]:
        if not seen[n]:
            counter[n] += x
            dfs(g, n, counter[n], cnt + 1)


dfs(graph, 1, counter[1], 1)
for i in range(1, N):
    print(counter[i], end=" ")
print(counter[N])
