A, B = map(int, input().split())
if A != B and (A + B) % 2 == 0:
    print((A + B) // 2)
else:
    print("IMPOSSIBLE")
