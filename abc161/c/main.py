N, M = map(int, input().split())
if N < M:
    N += M
if N % M == 0:
    print(0)
else:
    print(min(N % M, M - N % M))
