N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(max(0, M * N - sum(A)) if M * N - sum(A) <= K else -1)
