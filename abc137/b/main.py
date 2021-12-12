K, X = map(int, input().split())
a = [i for i in range(max(-1000000, X - K + 1), min(1000000, X + K))]
print(*a)
