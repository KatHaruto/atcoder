a, b, c = input().split()
print("Yes") if len(set([a, b, c])) == 2 else print("No")
