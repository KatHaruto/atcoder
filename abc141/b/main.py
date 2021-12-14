S = input()
if len(S) == 1:
    print("Yes") if S in "RUD" else print("No")
    exit()
for u, v in zip(S[1::2], S[::2]):
    if u not in "LUD":
        print("No")
        exit()
    if v not in "RUD":
        print("No")
        exit()
print("Yes")
