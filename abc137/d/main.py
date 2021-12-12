from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
labor = {}
for i in range(1, M + 1):
    labor[i] = []
for _ in range(N):
    a, b = map(int, input().split())
    if a <= M:
        labor[a].append(b)
h = []
heapify(h)

s = 0
for i in range(1, M + 1):
    for salary in labor[i]:
        heappush(h, -salary)
    s += heappop(h) if len(h) > 0 else 0
print(-s)
