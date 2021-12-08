N, M = map(int, input().split())
a = set([])
for _ in range(M):
    a.add(int(input()))

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 0 if 1 in a else 1
for i in range(2, N + 1):
    if i in a:
        dp[i] = 0
    else:
        if dp[i - 1] >= 0 or dp[i - 2] >= 0:
            dp[i] += (dp[i - 1] >= 0) * dp[i - 1] + (dp[i - 2] >= 0) * dp[i - 2]

        else:
            dp[i] = 0

print(dp[N] % (10 ** 9 + 7))
