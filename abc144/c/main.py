N = int(input())
min_div_sum = float("inf")
i = 1
while i ** 2 <= N:
    if N % i == 0:
        min_div_sum = min(min_div_sum, i + N // i)
    i += 1
print(min_div_sum - 2)
