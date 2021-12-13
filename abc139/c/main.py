N = int(input())
H = list(map(int, input().split()))
s = 0
max_s = 0
for i in range(N - 2, -1, -1):
    if H[i] >= H[i + 1]:
        s += 1
    else:
        s = 0
    max_s = max(s, max_s)

print(max_s)
