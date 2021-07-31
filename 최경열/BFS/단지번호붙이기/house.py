from collections import deque

graph = []
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            arr.append(bfs(i, j))

arr.sort()
print(len(arr))
for i in range(len(arr)):
    print(arr[i])
