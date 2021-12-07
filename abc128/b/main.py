N = int(input())
a = []
for i in range(N):
    x, y = input().split()
    a.append([x, int(y), i + 1])


a.sort(key=lambda x: x[1], reverse=True)
a.sort(key=lambda x: x[0])
for _, _, i in a:
    print(i)
