A, B = map(int, input().split())
i = 0
while i <= 10000:
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        exit()
    i += 1
print(-1)
