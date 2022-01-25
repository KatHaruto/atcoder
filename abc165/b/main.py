from math import ceil, log10

a = 100
x = int(input())
i = 0
while a < x:
    a = a + a // 100
    i += 1
print(i)
