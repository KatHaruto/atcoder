from math import log10

N = int(input())
cnt = 0
for nn in range(1, N + 1):
    if len(str(nn)) % 2 == 1:
        cnt += 1
print(cnt)
