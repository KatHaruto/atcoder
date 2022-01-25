from collections import Counter

N = int(input())
A = list(map(int, input().split()))
d = Counter(A)
for k, v in d.items():
    if v == 3:
        print(k)
        exit()
