from collections import deque

S = input()
Q = int(input())
d = deque([])
l = 0
r = 0
rev = False
for _ in range(Q):
    t = list(input().split())
    if len(t) == 1:
        rev = not rev
    elif t[1] == "1":
        if rev:
            d.append(t[2])
            r += 1
        else:
            d.appendleft(t[2])
            l += 1
    else:
        if rev:
            d.appendleft(t[2])
            l += 1
        else:
            d.append(t[2])
            r += 1
if rev:
    d.reverse()
    ans = "".join(list(d)[:r]) + S[::-1]
    if l > 0:
        ans += "".join(list(d)[-l:])
    print(ans)
else:
    ans = "".join(list(d)[:l]) + S
    if r > 0:
        ans += "".join(list(d)[-r:])
    print(ans)
