from collections import deque

H, W = map(int, input().split())
maze = []
for _ in range(H):
    maze.append(input())

d = deque()
max_dist = 0
for h in range(H):
    for w in range(W):
        if maze[h][w] == "#":
            continue
        d.append([w, h])
        dist = [[-1] * W for _ in range(H)]
        dist[h][w] = 0
        while d:
            sx, sy = d.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = sx + dx
                ny = sy + dy
                if nx < 0 or nx >= W or ny < 0 or ny >= H:
                    continue
                if maze[ny][nx] == "#":
                    continue
                if dist[ny][nx] != -1:
                    continue

                dist[ny][nx] = dist[sy][sx] + 1
                d.append([nx, ny])
        max_dist = max(max_dist, max(map(max, dist)))
print(max_dist)
