from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
m = Counter(S).most_common()[0][1]
l = list(filter(lambda x: x[1] == m, Counter(S).most_common()))
print(*sorted(map(lambda x: x[0], l)), sep="\n")
