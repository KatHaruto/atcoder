from collections import defaultdict


N, X, Y = map(int, input().split())
dp = [[-1] * N for _ in range(N)]
for i in range(N):
    dp[X - 1][i] = min(abs(X - 1 - i), abs(Y - 1 - i) + 1)
    dp[i][X - 1] = min(abs(X - 1 - i), abs(Y - 1 - i) + 1)
    dp[Y - 1][i] = min(abs(X - 1 - i) + 1, abs(Y - 1 - i))
    dp[i][Y - 1] = min(abs(X - 1 - i) + 1, abs(Y - 1 - i))


for i in range(N):
    for j in range(N):
        dp[i][j] = min(
            abs(i - j), dp[i][X - 1] + dp[X - 1][j], dp[i][Y - 1] + dp[Y - 1][j]
        )
cnt = defaultdict(int)
for i in range(N):
    for j in range(i + 1, N):
        cnt[dp[i][j]] += 1
print(*[cnt[i] for i in range(1, N)], sep="\n")
