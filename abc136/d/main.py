S = input()
dist = [0] * len(S)
r_cnt = 0
l_cnt = 0
for i in range(len(S)):
    if S[i] == "R":
        r_cnt = 0
    elif S[i] == "L":
        r_cnt -= 1
        dist[i] = r_cnt


for i in range(len(S) - 1, -1, -1):
    if S[i] == "L":
        l_cnt = 0
    elif S[i] == "R":
        l_cnt += 1
        dist[i] = l_cnt
mass = [0] * (len(S))
for i, d in enumerate(dist):
    mass[(i + d) + (-1) ** (d > 0) * (d % 2 == 1)] += 1

print(*mass)
