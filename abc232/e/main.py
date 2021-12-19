H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mod = 998244353
if K == 1:
    print(int(x2 == x1 or y2 == y1))
    exit()
print(
    (
        pow(W + H - 2, K - 2, mod)
        * (
            (H * W - (H + W - 1)) * 2
            + (H - 1) * (H - 2)
            + (W - 1) * (W - 2)
            + H
            + W
            - 2
        )
        % mod
    )
    % mod
)
