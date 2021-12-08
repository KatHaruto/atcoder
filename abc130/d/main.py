N, K = map(int, input().split())
A = list(map(int, input().split()))
s = [0]
for i in range(N):
    s.append(s[-1] + A[i])


ri = 1
le = 0
cnt = 0
while le < N:
    while ri < N:
        if s[ri] - s[le] >= K:
            break
        ri += 1
    if s[ri] - s[le] >= K:
        cnt += N - ri + 1
    le += 1
print(cnt)
