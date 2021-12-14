from bisect import bisect_left, bisect_right

N = int(input())
L = list(map(int, input().split()))
L.sort()
cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        b = L[i]
        c = L[j]
        l = bisect_left(L, c - b, lo=j + 1) + (j + 1)
        r = bisect_left(L, c + b, lo=j + 1) + (j + 1)
        cnt += r - l
print(cnt)
