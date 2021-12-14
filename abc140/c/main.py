N = int(input())
B = list(map(int, input().split()))
s = B[0]
for i in range(1, N - 1):
    s += min(B[i - 1], B[i])
print(s + B[-1])
