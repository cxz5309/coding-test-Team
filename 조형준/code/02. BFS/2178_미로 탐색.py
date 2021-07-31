from sys import stdin
from collections import deque


dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def bfs(n, m, arr):
    q = deque()
    q.append((0, 0, 1))
    cost = 1

    while q:
        x, y, cost = q.popleft()
        if (x, y) == (n - 1, m - 1):
            return cost

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < n and -1 < ny < m and arr[nx][ny] == 1:
                q.append((nx, ny, cost + 1))
                arr[nx][ny] = 0

    return cost


n, m = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))

print(bfs(n, m, arr))