N = int(input())
A = list(map(int, input().split()))
s = sum([(-1) ** i * A[i] for i in range(N)])
for i in range(N):
    if i < N - 1:
        print(s, end=" ")
    else:
        print(s)
    s = 2 * (A[i] - s // 2)
