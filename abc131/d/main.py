N = int(input())
ab = []
for _ in range(N):
    ab.append(list(map(int, input().split())))
ab.sort(key=lambda x: x[1])
t = 0
for i in range(N):
    t += ab[i][0]

    if t > ab[i][1]:
        print("No")
        break
else:
    print("Yes")
