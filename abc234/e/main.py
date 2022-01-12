def isAN(x):
    x = list(map(int, list(str(x))))
    if len(x) == 1:
        return True
    d = x[1] - x[0]
    for i in range(1, len(x)):
        if x[i] - x[i - 1] != d:
            break
    else:
        return True
    return False


X = input()
if isAN(X):
    print(X)
    exit()
m = float("inf")
for a in range(9, int(X[0]) - 1, -1):
    max_d = int((9 - int(a)) / (len(X) - 1))
    min_d = int((int(a)) / (len(X) - 1))

    for i in range(max_d, min(-1, -min_d - 1), -1):
        s = str(a)
        for _ in range(len(X) - 1):
            s += str(int(s[-1]) + i)
        if int(s) >= int(X):
            m = min(m, int(s))
print(m)
