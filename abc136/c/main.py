N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
for i in range(1, N):
    if H[i] > H[i - 1]:
        H[i] -= 1
        lower = H[i] - 1
    elif H[i] < H[i - 1]:
        print("No")
        break
else:
    print("Yes")
