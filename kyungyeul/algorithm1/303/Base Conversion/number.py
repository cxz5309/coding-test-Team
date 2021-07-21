import math
a, b = map(int, input().split(" "))

n = int(input())
arr = list(map(int, input().split(" ")))
ten, count = 0, 0

for i in arr[::-1]:
    c = int(i)
    ten += c * (a ** count)
    count += 1

arr2 = []
while ten:
    arr2.append(str(ten % b))
    ten //= b
    print(' '.join(arr2[::-1]))
