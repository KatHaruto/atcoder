from math import atan, pi

a, b, x = map(int, input().split())
if a ** 2 * b / 2 <= x:
    print((180 / pi) * atan((2 * a ** 2 * b - 2 * x) / a ** 3))
else:
    print((180 / pi) * atan(a * b ** 2 / (2 * x)))
