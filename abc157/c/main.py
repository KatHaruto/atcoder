N, M = map(int, input().split())
sc = {}
for _ in range(M):
    s, c = map(int, input().split())
    if s in sc.keys() and sc[s] != c:
        print(-1)
        exit()
    if N > 1 and s == 1 and c == 0:
        print(-1)
        exit()
    sc[s] = c
if N == 1 and (M == 0 or sc[1] == 0):
    print(0)
    exit()
ans = list("1" + "0" * (N - 1))
for s, c in sc.items():
    ans[s - 1] = str(c)
print(int("".join(ans)))
