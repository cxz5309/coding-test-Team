import math
a = int(input())
arr = []
sol = 0


def gcd(x, y):
    return math.gcd(x, y)


for i in range(a):
    arr.append(list(map(int, input().split(" "))))
    for j in range(1, len(arr[i])):
        for k in range(j+1, len(arr[i])):
            result = gcd(arr[i][j], arr[i][k])
            sol += result
    print(sol)
    sol = 0
