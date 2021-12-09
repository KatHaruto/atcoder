from functools import reduce

N, K = map(int, input().split())

# 1. 青の分け方 K-1Ci-1
# 2. 青の入れ方 N-K+1Ci

mod = 10 ** 9 + 7


def cmb(n, k, mod):
    numerator = reduce(lambda x, y: x * y % mod, [n - k + r + 1 for r in range(k)])
    denominator = reduce(lambda x, y: x * y % mod, [r + 1 for r in range(k)])
    return numerator * pow(denominator, mod - 2, mod) % mod


print(N - K + 1)
for i in range(2, K + 1):
    print(cmb(K - 1, i - 1, mod) * cmb(N - K + 1, i, mod) % mod)
