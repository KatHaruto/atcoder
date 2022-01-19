def kaibunn(s):
    return s[: len(s) // 2] == s[::-1][: len(s) // 2]


s = input()
if kaibunn(s) and kaibunn(s[: len(s) // 2]) and kaibunn(s[::-1][: len(s) // 2]):
    print("Yes")
else:
    print("No")
