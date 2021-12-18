from itertools import permutations

N = int(input())
P = "".join(input().split())
Q = "".join(input().split())
l = list(map(lambda x: "".join(map(str, x)), permutations(range(1, N + 1), N)))
print(abs(l.index(P) - l.index(Q)))
