N = int(input())
A = [[0] * (2 * N) for _ in range(2 * N)]
for i in range(2 * N - 1):
    A[i][i + 1 :] = list(map(int, input().split()))

used = [False] * (2 * N)
pairs = []


def rec():
    if len(pairs) == N:
        ans = 0
        for p in pairs:
            ans ^= A[p[0]][p[1]]
        return ans

    l = used.index(False)
    used[l] = True
    ret = 0
    for i in range(2 * N):
        if not used[i]:
            used[i] = True
            pairs.append([l, i])
            ret = max(rec(), ret)
            pairs.pop()
            used[i] = False
    used[l] = False
    return ret


print(rec())
