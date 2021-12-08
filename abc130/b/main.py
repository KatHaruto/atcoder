N, X = map(int, input().split())
L = list(map(int, input().split()))
s = 0
for i in range(len(L) - 1):
    L[i + 1] += L[i]
for i, l in enumerate(L):
    if l > X:
        print(i + 1)
        exit()
print(len(L) + 1)
