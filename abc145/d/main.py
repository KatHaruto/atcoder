from functools import reduce

X, Y = map(int, input().split())


def cmb(n, r, p=10 ** 9 + 7):
    nu = reduce(lambda x, y: x * y % p, [k for k in range(n, n - r, -1)])
    de = reduce(lambda x, y: x * y % p, [k for k in range(r, 0, -1)])
    return nu * pow(de, p - 2, p) % p


if (
    (2 * X - Y) % 3 != 0
    or (-X + 2 * Y) % 3 != 0
    or not (
        (X + Y) // 3 <= X <= 2 * ((X + Y) // 3)
        and (X + Y) // 3 <= Y <= 2 * ((X + Y) // 3)
    )
):
    print(0)
    exit()
m = (2 * X - Y) // 3
n = (-X + 2 * Y) // 3
if m == 0:
    print(1)
elif n == 0:
    print(1)
else:
    print(cmb(m + n, n))
