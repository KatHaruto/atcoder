N = int(input())
d = list(map(int, input().split()))
d.sort()
print(d[N // 2 - (N % 2 == 0) + 1] - d[N // 2 - (N % 2 == 0)] + (N % 2 == 1))
