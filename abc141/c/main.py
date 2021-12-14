N, K, Q = map(int, input().split())
score = [K - Q] * N
for _ in range(Q):
    score[int(input()) - 1] += 1
for s in score:
    if s <= 0:
        print("No")
    else:
        print("Yes")
