N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    if A[i] <= A[i + 1]:
        continue
    else:
        A = list(filter(lambda x: x != A[i], A))
        break
else:
    A = list(filter(lambda x: x != A[-1], A))
if not A:
    print()
else:
    print(*A)
