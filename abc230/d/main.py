N, D = map(int, input().split())
w = []
for _ in range(N):
    w.append(list(map(int, input().split())))
w.sort(key=lambda x: x[1])
ans = 0
i = -float("inf")
for ww in w:
    if i + D - 1 < ww[0]:
        ans += 1
        i = ww[1]
print(ans)
