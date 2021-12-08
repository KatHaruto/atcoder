H, W = map(int, input().split())
g = []
for _ in range(H):
    g.append(input())
hh = [[0] * W for _ in range(H)]
ww = [[0] * W for _ in range(H)]
for i in range(H):
    j = 0
    k = 1
    while j < W:
        if g[i][j] == "#":
            k = 0
        hh[i][j] = k
        j += 1
        k += 1
    for j in range(W - 2, -1, -1):
        if hh[i][j + 1] != 0 and hh[i][j] != 0:
            hh[i][j] = hh[i][j + 1]

for i in range(W):
    j = 0
    k = 1
    while j < H:
        if g[j][i] == "#":
            k = 0
        ww[j][i] = k
        j += 1
        k += 1
    for j in range(H - 2, -1, -1):
        if ww[j + 1][i] != 0 and ww[j][i] != 0:
            ww[j][i] = ww[j + 1][i]
m = -1
for i in range(H):
    for j in range(W):
        m = max(hh[i][j] + ww[i][j] - 1, m)
print(m)
