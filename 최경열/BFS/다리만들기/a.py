from collections import deque

graph = []
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
for i in range(10):
    graph.append(list(map(int, input().split())))

world = [[0]*n for _ in range(n)]
count = 1

# world에 연결된 육지끼리 같은번호 할당


def bfs(x, y, count):
    queue = deque()
    queue.append((x, y))
    world[x][y] = count
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and world[nx][ny] == 0:
                world[nx][ny] = count
                queue.append((nx, ny))

# 섬 중에서 하나를 선택해 섬의 크기를 늘려가면서
# 다른 섬에 닿을 때까지의 거리를 구한다.


def bfs2(num):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            # 육지이나 k육지가 아닌것
            if graph[nx][ny] == 1 and world[nx][ny] != num:
                return world2[x][y]-1
            if graph[nx][ny] == 0 and world2[nx][ny] == 0:
                world2[nx][ny] = world2[x][y]+1
                queue.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and world[i][j] == 0:
            bfs(i, j, count)
            count += 1


for k in range(1, count):
    print(k)
    queue = deque()
    world2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and world[i][j] == k:
                queue.append((i, j))
                world2[i][j] = 1
    print(bfs2(k))
