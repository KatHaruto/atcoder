N = int(input())
S = list(input())
for i in range(len(S)):
    S[i] = chr((ord(S[i]) - 65 + N) % 26 + 65)
print("".join(S))
