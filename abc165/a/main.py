K = int(input())
A, B = map(int, input().split())
if A <= K * (A // K + int(A % K != 0)) <= B:
    print("OK")
else:
    print("NG")
