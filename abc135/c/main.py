N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if A[i] < B[i]:
        cnt += A[i] + min(B[i] - A[i], A[i + 1])
        A[i + 1] -= min(B[i] - A[i], A[i + 1])
    else:
        cnt += B[i]
print(cnt)
