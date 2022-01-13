from itertools import product

N = int(input())
num = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    if i % 10 != 0:
        num[int(str(i)[0])][i % 10] += 1
cnt = 0
for i, j in product(range(1, 10), repeat=2):
    cnt += num[i][j] * num[j][i]
print(cnt)
