from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10 ** 6)


n = int(stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().strip().split())))

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
num = 97
res = 1e9


def island_cnt(x, y):
    if 0 > x or x >= n or 0 > y or y >= n:
        return False

    if arr[x][y] == 1:
        arr[x][y] = chr(num)
        for i in range(4):
            island_cnt(x + dx[i], y + dy[i])

        return True
    return False


def bfs(k):
    global res
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for x in range(n):
        for y in range(n):
            if arr[x][y] == k:
                q.append((x, y))
                dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            if arr[nx][ny] != 0 and arr[nx][ny] != k:
                res = min(res, dist[x][y])
                return

            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


island_ea = 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1 and island_cnt(x, y):
            island_ea += 1
            num += 1


for i in range(97, 97 + island_ea):
    bfs(chr(i))


print(res)