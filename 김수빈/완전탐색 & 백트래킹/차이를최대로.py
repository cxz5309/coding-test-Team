from itertools import permutations

n = int(input())
data = list(map(int,input().split()))
data1 = permutations(data,n)

max = 0
for sample in data1:
    result = 0
    for i in range(len(sample)-1):
        result += abs(sample[i]-sample[i+1])
    if max < result:
        max = result
print(max)