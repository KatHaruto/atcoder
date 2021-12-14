N = int(input())
A = list(map(int, input().split()))
A = [[a, i + 1] for i, a in enumerate(A)]
A.sort(key=lambda x: x[0])
print(*list(map(lambda x: x[1], A)))
