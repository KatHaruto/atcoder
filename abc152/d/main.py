N = int(input())
cnt = 0
for a in range(1, N + 1):
    if a < 10:
      cnt += 1
    if str(a)[-1] == "0":
        continue
    if len(str(a)) < len(str(N)):
        if len(str(a)) == 2:
          cnt += 3
        elif len(str(a)) == 3:
          cnt += 
        if str(a)[0] == str(a)[-1]:
            cnt += 2*(1+int('1'*len(str(a))-2)+int(str(a)]))
        cnt += 10 ** (max(0, len(str(a)) - 2)) + int(str(a)[0] != str(a)[-1])
    else:
        if str(N)[0] < str(a)[-1] or str(N)[-1] < str(a)[0]:
            continue
        # cnt +=

print(cnt)
