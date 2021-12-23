from math import log2

H = int(input())
print(2 ** int(log2(H) + 1) - 1)
