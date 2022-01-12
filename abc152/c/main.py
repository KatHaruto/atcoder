N = int(input())
P = list(map(int, input().split()))
m = 2 * 10 ** 5 + 1
cnt = 1
for i in range(1, N):
    m = min(m, P[i - 1])
    if P[i] <= m:
        cnt += 1
print(cnt)
