at = ["a", "t", "c", "o", "d", "e", "r"]
S = input()
T = input()
for s, t in zip(S, T):
    if s != "@" and t != "@" and s != t:
        print("You will lose")
        exit(0)
    if s == t or (s == "@" and t in at) or (t == "@" and s in at):
        continue
    else:
        print("You will lose")
        exit(0)


print("You can win")
