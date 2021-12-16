S = input()
cnt = 0
for s1, s2 in zip(
    S[: len(S) // 2], S[len(S) - 1 : len(S) // 2 - (len(S) % 2 == 0) : -1]
):
    if s1 != s2:
        cnt += 1

print(cnt)
