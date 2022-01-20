N, M = map(int, input().split())
A = list(map(int, input().split()))
print("Yes") if len(list(filter(lambda x: x >= sum(A) / (4 * M), A))) >= M else print(
    "No"
)
