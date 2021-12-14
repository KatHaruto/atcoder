N, K = map(int, input().split())
h = list(map(int, input().split()))
print(sum([hh >= K for hh in h]))
