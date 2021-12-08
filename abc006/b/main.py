t = [0, 0, 1]

N = int(input())
if N <= 3:
    print(t[N - 1])
    exit()
a, b, c = 0, 0, 1
s = 0
for i in range(4, N + 1):
    s = (a + b + c) % 10007
    a = b
    b = c
    c = s
print(s % 10007)
