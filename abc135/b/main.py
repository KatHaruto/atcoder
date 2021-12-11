N = int(input())
p = list(map(int, input().split()))
cnt = 0
for u, v in zip(p, sorted(p)):
    if u != v:
        cnt += 1
if cnt <= 2:
    print("YES")
else:
    print("NO")
