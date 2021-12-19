from collections import deque

H, W = map(int, input().split())
maze = []
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for _ in range(H):
    maze.append(input())
x = 0
y = 0
# que = deque()
que = []
que.append([0, 1])
que.append([1, 0])
cnt = 1
visited = [[False] * W for _ in range(H)]
while que:
    x, y = que.pop(-1)
    if x >= W or y >= H:
        continue
    visited[y][x] = True
    if maze[y][x] == "#":
        dp[y][x] = -float("inf")
    else:
        if x == 0:
            dp[y][x] = dp[y - 1][x] + 1
        elif y == 0:
            dp[y][x] = dp[y][x - 1] + 1
        else:
            dp[y][x] = max(dp[y][x - 1] + 1, dp[y - 1][x] + 1)
        if x + 1 < W and not visited[y][x + 1]:
            que.append([x + 1, y])
        if y + 1 < H and not visited[y + 1][x]:
            que.append([x, y + 1])
print(max([max(d) for d in dp]))
