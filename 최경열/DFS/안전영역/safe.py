import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
max_value = []

for i in range(n):
    graph.append(list(map(int, input().split(" "))))
for i in graph:
    max_value.append(max(i))

rain_max = max(max_value)


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] > m and chk[x][y] == 1:
        chk[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


res = []
for m in range(rain_max):
    result = 0
    chk = [[1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    res.append(result)
print(max(res))
