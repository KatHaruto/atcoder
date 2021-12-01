N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
R = R[-K:]
s = 0.0

for r in R:
    s = (s + r) / 2
print(s)
