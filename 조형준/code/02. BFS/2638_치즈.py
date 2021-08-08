from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().strip().split())
graph = []
for x in range(n):
    data = list(map(int, stdin.readline().strip().split()))
    graph.append(data)


dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]


def fresh_air():
    q = deque()
    q.append((0, 0))

    visited = [[0] * m for _ in range(n)]
    graph[0][0] = -1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if (nx < 0 or ny < 0 or nx >= n or ny >= m) or (graph[nx][ny] == 1 or visited[nx][ny]):
                continue
            q.append((nx, ny))
            graph[nx][ny] = -1
            visited[nx][ny] = 1


def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return False
    return True


res = 0
while not check():
    fresh_air()
    check_list = []

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                cnt = 0
                for i in range(4):
                    nx, ny = dx[i] + x, dy[i] + y
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if graph[nx][ny] == -1:
                        cnt += 1

                if cnt >= 2:
                    check_list.append((x, y))

    for x, y in check_list:
        graph[x][y] = 0

    res += 1

print(res)