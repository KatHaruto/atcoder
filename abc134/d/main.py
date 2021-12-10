N = int(input())
a = list(map(int, input().split()))
b = [0] * N
for i in range(N, 0, -1):
    if sum(b[i - 1 :: i]) % 2 != a[i - 1]:
        b[i - 1] = (b[i - 1] + 1) % 2
print(sum(b))
if sum(b) > 0:
    for i, bb in enumerate(b):
        if bb == 0:
            continue
        print(i + 1, end=" ")
    print()
