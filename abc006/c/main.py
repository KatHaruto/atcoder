N, M = map(int, input().split())
P = M - 2 * N
if P == 0 and M // 2 == N and M % 2 == 0:
    print(M // 2, 0, 0)
    exit()
for i in range(P):
    if (P - i) % 2 == 0:
        if N - i - (P - i) // 2 >= 0:
            print(N - i - (P - i) // 2, i, (P - i) // 2)
            exit()
    elif N - P >= 0:
        print(N - P, P, 0)
        exit()
print(-1, -1, -1)
