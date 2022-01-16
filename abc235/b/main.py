N = int(input())
A = list(map(int, input().split()))
i = 0
while i < N - 1 and A[i] < A[i + 1]:
    i += 1
print(A[i])
