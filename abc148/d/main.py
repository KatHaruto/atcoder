N = int(input())
a = list(map(int, input().split()))
i = 1
cnt = 0
for aa in a:
    if aa == i:
        i += 1
    else:
        cnt += 1
print(cnt if cnt < N else -1)
