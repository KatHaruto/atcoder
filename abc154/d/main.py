N, K = map(int, input().split())
p = list(map(int, input().split()))
p = [pi * (pi + 1) / (2 * pi) for pi in p]
ans = sum(p[:K])
s = ans
for i in range(K, N):
    ans = max(ans, s - p[i - K] + p[i])
    s = s - p[i - K] + p[i]
print(ans)
