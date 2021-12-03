T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
i = 0
j = 0


while True:
    if j == len(B):
        print("yes")
        exit()
    elif i == len(A) or (i < len(A) and A[i] > B[j]):
        print("no")
        exit()
    if A[i] + T < B[j]:
        i += 1
    else:
        i += 1
        j += 1
