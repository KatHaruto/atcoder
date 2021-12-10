N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

m2, m1 = sorted(A)[-2:]
for i in range(N):
    print(m1 if A[i] != m1 else m2)
