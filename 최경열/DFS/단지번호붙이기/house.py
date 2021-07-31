n = int(input())
graph = []
arr = []
count = 0
result = 0
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            arr.append(count)
            count = 0
arr.sort()
print(result)
for i in arr:
    print(i)
