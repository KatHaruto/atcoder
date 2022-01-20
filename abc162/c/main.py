from functools import reduce
import math


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


ans = 0
K = int(input())
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += my_gcd(*[i, j, k])

print(ans)
