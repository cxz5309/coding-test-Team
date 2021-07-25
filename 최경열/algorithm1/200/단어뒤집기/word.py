a = int(input())
for i in range(a):
    data = list(input().split(' '))
    for j in data:
        word = reversed(j)
        print(''.join(list(word)), end=" ")
    print()
