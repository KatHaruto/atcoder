N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(1, N):
    A[i] += A[i - 1]
l = 0
r = l
cnt = 0
while l <N:
    if A[l] == K:
        cnt += 1
        continue
    while r < N:
        if l == 0:
            if A[r] == K:
              cnt += 1
              l+=1
        elif A[r]-A[l-1] == K:
            cnt += 1
            r+=1
        else:
            
        
