x, y = map(int, input().split())
z = y - x
print(max(0, z // 10 + int(z % 10 > 0)))
