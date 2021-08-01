import sys
import copy
from collections import deque
a, b = map(int, sys.stdin.readline().split())
graph = []
temp = [[0]*b for _ in range(a)]

for _ in range(a):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0

# 바이러스 퍼트리기


def virus(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < a and ny >= 0 and ny < b:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

# 안전영역 크기계산


def get_score():
    score = 0
    for i in range(a):
        for j in range(b):
            if temp[i][j] == 0:
                score += 1
    return score

# 울타리 설치해서, 바이러스 퍼트린후 안전영역 크기계산


def dfs(count):
    global result
    # 울타리를 다 설치 했다면
    if count == 3:
        for i in range(a):
            for j in range(b):
                temp[i][j] = graph[i][j]
        for i in range(a):
            for j in range(b):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
     # 울타리를 설치하기
    for i in range(a):
        for j in range(b):
            # 울타리를 설치
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                # 울타리를 리셋
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)
