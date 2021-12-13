A, B = map(int, input().split())
print((B - 1) // (A - 1) + ((B - 1) % (A - 1) > 0))
