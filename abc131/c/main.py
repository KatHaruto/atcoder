from math import gcd

A, B, C, D = map(int, input().split())
n1 = B // C - (A // C - (A % C == 0))
n2 = B // D - (A // D - (A % D == 0))
lcm_cd = int(C * D / gcd(C, D))
n3 = B // (lcm_cd) - (A // (lcm_cd) - (A % (lcm_cd) == 0))
print(B - A + 1 - n1 - n2 + n3)
