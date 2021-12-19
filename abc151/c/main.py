N, M = map(int, input().split())
ac = [[False, 0] for _ in range(N)]
for i in range(M):
    p, s = input().split()
    p = int(p)
    if s == "AC":
        ac[p - 1][0] = True
    if s == "WA":
        ac[p - 1][1] += int(not ac[p - 1][0])
print(sum(map(lambda x: int(x[0]), ac)), sum(map(lambda x: x[1] * x[0], ac)))
