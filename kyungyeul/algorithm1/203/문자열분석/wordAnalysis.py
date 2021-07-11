import sys
while True:
    a = sys.stdin.readline().rstrip('\n')
    if not a:
        break
    l, u, n, s = 0, 0, 0, 0
    for i in a:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            n += 1
        elif i.isspace():
            s += 1
    print(l, u, n, s)
