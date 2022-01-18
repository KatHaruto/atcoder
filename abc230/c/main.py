N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
# B + max(1 - A, 1 - B) <= j <= B + min(N - A, N - B)
# B - min(N - A, B - 1) <= j <= B - max(1 - A, B - N)
for i in range(P, Q + 1):
    for j in range(R, S + 1):
        if (A + max(1 - A, 1 - B) <= i <= A + min(N - A, N - B) and j == i - A + B) or (
            A + max(1 - A, B - N) <= i <= A + min(N - A, B - 1) and j == -i + A + B
        ):
            print("#", end="")
        else:
            print(".", end="")
    print()
