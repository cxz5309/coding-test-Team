result, cnt_0 = 1, 0
for i in range(int(input()), 1, -1):
    result *= i

for s in str(result)[::-1]:
    if s == '0':
        cnt_0 += 1
    else:
        break
print(cnt_0)