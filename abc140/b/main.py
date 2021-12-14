N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
s = B[A[0] - 1]
for i in range(1, N):
    s += B[A[i] - 1]
    if A[i - 1] + 1 == A[i]:
        s += C[A[i - 1] - 1]
print(s)
