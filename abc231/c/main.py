from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(Q):
    x = int(input())
    print(N - bisect_left(A, x))
