def movecount(G, j):
    j = abs(j)
    if G > j:
        return G * G // 4 + j * j // 4
    else:
        return G * (G + 1) // 2 + ((j - G) // 2) * G


R, G, B = [int(x) for x in input().split()]
a, b = [R + G, G + B]
jmin = min(200 - a, -1)
jmax = max(b - 200, 1)
minval = 10000000000000
for j in range(jmin, jmax + 1):
    if j % 2 == G % 2:
        continue
    k = min(j + 200 - b, 0)
    i = max(j + a - 200, 0)
    val = movecount(B, k) + movecount(G, j) + movecount(R, i)
    print(movecount(B, k), k, movecount(G, j), j, movecount(R, i), i, val)

    minval = min(val, minval)
print(minval)
