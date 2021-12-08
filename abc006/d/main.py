from bisect import bisect_left

N, *c = list(map(int, open(0).read().split("\n")[:-1]))
dp = [float("inf")] * N

for i in range(N):
    dp[bisect_left(dp, c[i])] = c[i]
print(N - bisect_left(dp, float("inf")))
