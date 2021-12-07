N, K = map(int, input().split())
V = list(map(int, input().split()))
max_s = -1
for L in range(min(N, K) + 1):
    for R in range(min(N, K) - L + 1):
        cnt = 0
        l = V[:L] + V[-R:] if R > 0 else V[:L]
        su = sum(l)
        for s in sorted(l):
            if s > 0 or cnt == K - (L + R):
                break
            su -= s
            cnt += 1
        # print(L, R, l, su, end="\n\n")
        max_s = max(max_s, su)
print(max_s)
