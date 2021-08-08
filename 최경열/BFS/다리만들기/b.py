from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
n = int(input())
for i in range(10):
    graph.append(list(map(int, input().split())))

c1 = [[0]*n for _ in range(n)]
cnt = 1

# ----


def bfs1(x, y, cnt):
    queue = deque()
    queue.append([x, y])
    c1[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and c1[nx][ny] == 0:
                    c1[nx][ny] = cnt
                    queue.append([nx, ny])


def bfs2(num):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and c1[nx][ny] != num:
                    return c2[x][y]-1
                if graph[nx][ny] == 0 and c2[nx][ny] == 0:
                    c2[nx][ny] = c2[x][y] + 1
                    queue.append([nx, ny])


# ----
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and c1[i][j] == 0:
            bfs1(i, j, cnt)
            cnt += 1

ans = sys.maxsize
for k in range(1, cnt):
    queue = deque()
    c2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and c1[i][j] == k:
                queue.append([i, j])
                c2[i][j] = 1
    res = bfs2(k)
    ans = min(ans, res)

print(ans)
print(c1)
