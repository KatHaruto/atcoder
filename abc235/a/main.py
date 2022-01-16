a, b, c = list(input())
print(int("".join([a, b, c])) + int("".join([b, c, a])) + int("".join([c, a, b])))
