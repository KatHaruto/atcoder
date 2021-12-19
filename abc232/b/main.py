S = input()
T = input()
K = (ord(T[0]) - ord(S[0])) % 26
for i in range(1, len(S)):
    if (ord(T[i]) - ord(S[i])) % 26 != K:
        print("No")
        exit()
print("Yes")
