import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]
heapq.heapify(A)
for _ in range(M):
    m = heapq.heappop(A)
    heapq.heappush(A, int(m / 2))
print(-sum(A))
