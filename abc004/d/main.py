R, G, B = map(int, input().split())
min_n = float("inf")


def su(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2

    # Gの左にi個分ける


for i in range(G):
    rr = R // 2 - int(R % 2 == 0) if 99 - i > (R // 2 - int(R % 2 == 0)) else 99 - i
    rl = R - max(rr, 0) - 1
    bl = (
        B // 2 - int(B % 2 == 0)
        if 99 - (G - i - 1) > (B // 2 - int(B % 2 == 0))
        else 99 - (G - i - 1)
    )
    br = B - max(bl, 0) - 1
    print(
        rl,
        rr,
        i,
        G - i - 1,
        bl,
        br,
        su(rl)
        + su(rr)
        + int(rr < 0) * (-rr) * R
        + su(i)
        + su(G - i - 1)
        + su(bl)
        + su(br)
        + int(bl < 0) * (-bl) * B,
    )
    min_n = min(
        min_n,
        su(rl)
        + su(rr)
        + int(rr < 0) * (-rr) * R
        + su(i)
        + su(G - i - 1)
        + su(bl)
        + su(br)
        + int(bl < 0) * (-bl) * B,
    )
print(min_n)
