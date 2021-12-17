from math import log10, prod

N = int(input())
if N % 2 == 1:
    print(0)
else:
    print(sum([N // (10 ** i) for i in range(1, int(log10(N)) + 1)]))
a = list(range(2, 128, 2))
for i in range(len(a) - 1):
    a[i + 1] *= a[i]
print(*zip(range(2, 128, 2), a), sep="\n")
# print(prod(range(2, 128, 2)))
