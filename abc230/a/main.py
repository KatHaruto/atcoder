n = input()
if int(n) >= 42:
    print("AGC" + str(int(n) + 1).rjust(3, "0"))
else:
    print("AGC" + n.rjust(3, "0"))
