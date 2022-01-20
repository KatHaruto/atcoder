def getNextLunLun(n):
    if n < 10:
        n += 1
        return n
    n = list(map(int, list(str(n))))
    for i in range(len(n) - 1):
        if 0 <= n[-i - 2] - n[-i - 1] <= 1:
            if n[-i - 1] == 9:
                continue
            n[-i - 1] += 1
            for j in range(-i, 0):
                n[j] = max(n[j - 1] - 1, 0)
            break
    else:
        if n[0] == 9:
            n[0] += 1
            for i in range(1, len(n)):
                n[i] = 0
        else:
            n[0] += 1
            for i in range(1, len(n)):
                n[i] = max(n[i - 1] - 1, 0)
    return int("".join(map(str, n)))


K = int(input())
ans = 1
for _ in range(K - 1):
    ans = getNextLunLun(ans)
print(ans)
