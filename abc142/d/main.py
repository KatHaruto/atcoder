from math import gcd
from itertools import combinations
from functools import reduce


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


A, B = map(int, input().split())
div = set(make_divisors(A)).intersection(set(make_divisors(B)))
cnt = 0
for d in div:
    for dd in div:
        if d == dd or dd == 1:
            continue
        if d % dd == 0:
            break
    else:
        cnt += 1
print(cnt)
