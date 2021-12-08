N = int(input())
l = []
for i in range(6):
    l.append(5 - (((5 - i) + (N // 5)) % 6))
for i in range(6):
    if l[i] > N % 5:
        continue
    elif l[i] == 0:
        l[i] += N % 5
    else:
        l[i] -= 1
for i in range(6):
    print(l.index(i) + 1, end="")
print()
