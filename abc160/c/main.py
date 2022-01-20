K, N = map(int, input().split())
A = list(map(int, input().split()))
d = [0] * N
for i in range(1, N):
    d[i] = A[i] - A[i - 1]
d.append(K + A[0] - A[-1])
print(sum(d) - max(d))
