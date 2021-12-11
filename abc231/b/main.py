from collections import Counter

N = int(input())
s = []
for _ in range(N):
    s.append(input())
print(Counter(s).most_common()[0][0])
