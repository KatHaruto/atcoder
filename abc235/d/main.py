from collections import deque


def rev(x, i):
    x = str(x)
    return x[-i:] + x[:-i]


def appendrev(x):
    sx = str(x)
    if x < 10:
        return
    rx = x
    for i in range(1, len(sx)):
        if rx % 10 == 0:
            break
        rx = int(rev(x, i))
        if rx <= 10 ** 6 and (v[rx] > v[x] + i):
            s.append(rx)
            v[rx] = v[x] + i


a, N = map(int, input().split())

v = {}
for i in range(1, 10 ** 6 + 1):
    v[i] = float("inf")
v[1] = 0
s = deque([1])
i = 0
while s:

    x = s.popleft()
    if x * a <= 10 ** 6 and (v[x] + 1 < v[x * a]):
        v[x * a] = v[x] + 1
        s.append(x * a)
    appendrev(x)
print(v[N]) if v[N] != float("inf") else print(-1)
