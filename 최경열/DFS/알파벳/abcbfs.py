# 문제는 해결이 되나 시간초과,메모리 초과 발생
# 이유는 모든 경로를 돌기 때문에

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
graph = []

# 입력
R, C = map(int, input().split())
for i in range(R):
    graph.append(list(input()))


def bfs(x, y):
    global result
    queue = deque()
    queue.append((x, y, graph[x][y]))
    while queue:
        x, y, ans = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if graph[nx][ny] not in ans:
                queue.append((nx, ny, ans + graph[nx][ny]))
                result = max(result, len(ans)+1)


result = 1
bfs(0, 0)
print(result)
