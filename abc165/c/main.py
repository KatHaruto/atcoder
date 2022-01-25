N, M, Q = map(int, input().split())
q = []
for _ in range(Q):
    q.append(list(map(int, input().split())))
A = []
ans = -1


def calc(A):
    ret = 0
    for a, b, c, d in q:
        if A[b - 1] - A[a - 1] == c:
            ret += d
    return ret


def rec(d):
    if len(A) == N:
        global ans
        ans = max(ans, calc(A))
        return
    for i in range(d, M + 1):
        A.append(i)
        rec(i)
        A.pop()
    return


rec(1)
print(ans)
