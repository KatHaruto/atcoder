N, K = map(int, input().split())
p = 10 ** 9 + 7
ans = 0
for k in range(K, N + 2):
    ans += (N * (N + 1) // 2 - (N - k) * (N - k + 1) // 2 + 1 - k * (k - 1) // 2) % p
print(ans % p)
