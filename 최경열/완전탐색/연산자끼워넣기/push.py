from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))

operation = list(map(int, input().split()))
operation2 = ["+", "-", "*", "/"]
king = []
ww = []
for i in range(len(operation)):
    if operation[i] == 1:
        print(operation2[i])

for i in list(combinations(operation2, len(arr)-1)):
    king.append(i)

print(king)
