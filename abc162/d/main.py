from bisect import bisect

N = int(input())
S = input()
rgb = {"R": [], "G": [], "B": []}
c = set(["R", "G", "B"])
for i, s in enumerate(S):
    rgb[s].append(i)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            s = (c - set([S[i], S[j]])).pop()
            k = bisect(rgb[s], j)
            ans += len(rgb[s]) - k - int(j + j - i < N and S[j + (j - i)] == s)
print(ans)
