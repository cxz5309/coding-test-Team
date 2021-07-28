from itertools import permutations

a = int(input())
arr = permutations(list(map(int, input().split(" "))))
result = 0
for i in arr:
    sum = 0
    for j in range(a-1):
        sum = sum + abs(i[j]-i[j+1])
    result = max(result, sum)
print(result)
