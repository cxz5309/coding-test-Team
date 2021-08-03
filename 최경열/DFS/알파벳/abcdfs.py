import sys
sys.setrecursionlimit(10000)


# 입력
R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(map(lambda x: ord(x)-65, input())))
arr = [0] * 26

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, z):
    global answer
    answer = max(answer, z)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if arr[graph[nx][ny]] == 0:
            arr[graph[nx][ny]] = 1
            dfs(nx, ny, z+1)
            arr[graph[nx][ny]] = 0


answer = 1
arr[graph[0][0]] = 1
dfs(0, 0, answer)
print(answer)
