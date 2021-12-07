N, M, *LR = map(int, open(0).read().split())
L, R = LR[::2], LR[1::2]
print(max(0, min(R) - max(L) + 1))
