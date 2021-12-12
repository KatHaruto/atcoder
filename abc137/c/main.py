from collections import Counter

N = int(input())
S = Counter(["".join(sorted(input())) for _ in range(N)])
print(sum([(i * (i - 1)) // 2 for i in S.values()]))
