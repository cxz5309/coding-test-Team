import sys
import math
from itertools import combinations

n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

people = list(range(n))
candidate = list(combinations(people, n // 2))

answer = math.inf

for group in candidate:
    rest = list(set(people) - set(group))

    group_sum, rest_sum = 0, 0
    group_combination = list(combinations(list(group), 2))
    rest_combination = list(combinations(rest, 2))

    for y, x in group_combination:
        group_sum += (arr[y][x] + arr[x][y])

    for y, x in rest_combination:
        rest_sum += (arr[y][x] + arr[x][y])

    if answer > abs(group_sum - rest_sum):
        answer = abs(group_sum - rest_sum)
print(answer)

# for i in range(n):
#    for j in range(n):
#        print(arr[i][j],end="")
#    print()