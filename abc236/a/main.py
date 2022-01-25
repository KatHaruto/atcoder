s = list(input())
a, b = map(int, input().split())
tmp = s[b - 1]
s[b - 1] = s[a - 1]
s[a - 1] = tmp
print("".join(s))
