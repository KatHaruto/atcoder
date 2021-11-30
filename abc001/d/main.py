import sys

sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    se = [[int(v) for v in input().split("-")] for _ in range(n)]

    se.sort()

    for i in range(n):
        s, e = se[i]
        se[i][0] = s - s % 5
        if e % 5 == 0:
            se[i][1] = e
        else:
            se[i][1] = e + 5 - e % 5
            if se[i][1] % 100 == 60:
                se[i][1] += 40

    s = se[0][0]
    e = se[0][1]
    for i in range(1, n):
        if se[i][0] <= e:
            e = max(e, se[i][1])
        else:
            print(f"{s:04}-{e:04}")
            s = se[i][0]
            e = se[i][1]
    else:
        print(f"{s:04}-{e:04}")


main()
