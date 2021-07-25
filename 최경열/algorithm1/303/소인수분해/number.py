a = int(input())
b = 2
while a != 1:
    if a % b == 0:
        a = a/b
        print(b)
    else:
        b += 1
        print(b)
