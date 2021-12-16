from math import floor, log10

A, B, X = map(int, input().split())

a = 0
b = 10 ** 9 + 1

while a < b - 1:
    mid = (b + a) // 2

    if A * mid + B * floor(log10(mid) + 1) <= X:
        a = mid
    else:
        b = mid

print(a)
