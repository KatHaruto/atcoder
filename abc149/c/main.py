X = int(input())

i = 2
while True:
    j = 2
    while j ** 2 <= i:
        if i % j == 0:
            break
        j += 1
    else:
        if i >= X:
            print(i)
            exit()
    i += 1
