from collections import deque

graph = []
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 입력
a, b = map(int, input().split())
for i in range(a):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[a-1][b-1]


print(bfs(0, 0))
