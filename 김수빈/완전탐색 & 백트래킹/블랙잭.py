from itertools import combinations

a,b = map(int,input().split())
data = list(map(int,input().split()))
data1 = combinations(data,3)
max_sum = []

for sample in data1:
    if sum(sample) > b:
        continue
    else:
        max_sum.append(sum(sample))
print(max(max_sum))