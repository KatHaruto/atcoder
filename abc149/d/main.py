N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
d = {"r": 0, "s": 1, "p": 2}
s = {0: R, 1: S, 2: P}
ans = 0
for i in range(K):
    dp = [[0] * 3 for _ in range(i, N, K)]
    dp[0][(d[T[i]] + 2) % 3] = s[(d[T[i]] + 2) % 3]
    for j in range(1, (N - i) // K + ((N - i) % K > 0)):
        for k in range(3):
            if k == (d[T[i + K * j]] + 2) % 3:
                dp[j][k] = max(dp[j - 1][(k + 1) % 3], dp[j - 1][(k + 2) % 3]) + s[k]
            else:
                dp[j][k] = max(dp[j - 1][(k + 1) % 3], dp[j - 1][(k + 2) % 3])
    ans += max(dp[-1])
print(ans)
