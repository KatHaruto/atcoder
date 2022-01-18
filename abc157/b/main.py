import numpy as np

A = np.array([[0] * 3 for _ in range(3)])
d = {}
for i in range(3):
    a, b, c = map(int, input().split())
    d[a] = [i, 0]
    d[b] = [i, 1]
    d[c] = [i, 2]
N = int(input())
for _ in range(N):
    b = int(input())
    if b in d.keys():
        A[d[b][0]][d[b][1]] = 1
for i in range(3):
    if sum(A[:, i]) == 3 or sum(A[i, :]) == 3:
        print("Yes")
        exit()
if A[0][0] + A[1][1] + A[2][2] == 3 or A[2][0] + A[1][1] + A[0][2] == 3:
    print("Yes")
    exit()
print("No")
