n = int(input())
graph = []
max_value = []
min_value = []
for i in range(n):
    graph.append(list(map(int, input().split(" "))))

for i in graph:
    max_value.append(max(i))
    min_value.append(min(i))

print(max(max_value))
print(min(min_value))
