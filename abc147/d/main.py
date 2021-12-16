N = int(input())
A = list(map(lambda s: bin(int(s))[2:], input().split()))
n = max(map(len, A))
cnt = 0
for i in range(1, n + 1):
    p = 0
    q = 0
    for a in A:
        if len(a) < i:
            p += 1
            continue
        if a[-i] == "0":
            p += 1
        else:
            q += 1
    cnt += (pow(2, i - 1) * p * q) % (10 ** 9 + 7)
print(cnt % (10 ** 9 + 7))
