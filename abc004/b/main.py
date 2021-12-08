grid = [input().split() for _ in range(4)]
for i in range(3, -1, -1):
    print(" ".join(grid[i][::-1]))
