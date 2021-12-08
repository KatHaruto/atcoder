W, H, x, y = map(int, input().split())
print(W * H / 2, int(x != 0 and y != 0 and W / x == 2 and H / y == 2))
