p = 10 ** 9 + 7
N = 10 ** 4  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())


n = (R - X + 1) * (C - Y + 1)
print((n * (cmb(X * Y, D, p) * cmb(X * Y - D, L, p) % p)) % p)
