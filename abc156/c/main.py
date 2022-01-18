N = int(input())
X = list(map(int, input().split()))
ans = float("inf")
for x1 in range(min(X), max(X) + 1):
    ans = min(ans, sum(map(lambda x: (x - x1) ** 2, X)))
print(ans)
