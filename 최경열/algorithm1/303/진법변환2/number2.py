a, b = map(int, input().split(" "))
answer = ""
while a:
    res = a % b
    print('res', res)
    if res < 10:
        c = str(res)
    else:
        c = chr(res+55)
    answer += c
    a = a//b
    print(a)
print(answer[::-1])
