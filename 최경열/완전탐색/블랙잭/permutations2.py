from itertools import combinations

n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
result = 0

for i in combinations(arr, 3):
    temp_sum = sum(i)
    if temp_sum <= m:
        result = max(result, temp_sum)
print(result)
