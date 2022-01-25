N, M = map(int, input().split())
S = input().split()
T = set(input().split())
for ss in S:
    if ss in T:
        print("Yes")
    else:
        print("No")
