N = int(input())
W = list(map(int, input().split()))
m_d = float("inf")
for i in range(1, N):
    m_d = min(m_d, abs(sum(W[: i + 1]) - sum(W[i + 1 :])))
print(m_d)
