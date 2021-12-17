N = int(input())
S, T = input().split()
print("".join(map(lambda st: "".join(st), zip(S, T))))
