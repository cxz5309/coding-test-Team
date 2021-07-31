from sys import stdin
from collections import deque

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def bfs(x, y, arr):
    q = deque()
    q.append((x, y))
    leng = len(arr)
    visited = [(x, y)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < leng and -1 < ny < leng and arr[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.append((nx, ny))

    for i, j in visited:
        arr[i][j] = 9

    return visited


def solution(n, arr):
    cnt = 0
    res = []

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                k = bfs(x, y, arr)
                if k:
                    res.append(len(k))
                    cnt += 1

    print(cnt)
    res.sort()
    for i in range(cnt):
        print(res[i])


n = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))


solution(n, arr)


