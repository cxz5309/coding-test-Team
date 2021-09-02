# 재귀 깊이 제한을 푸는 것 
from sys import setrecursionlimit 
setrecursionlimit(10**9) 

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
memory = [[-1]* n for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = dx[::-1]

def dfs(i, j):
    if memory[i][j] < 0:
        memory[i][j] = 0
        for d in range(4):
            x, y = i+dx[d], j+dy[d]
            # 이동범위가 프레임을 넘지 않고 대나무가 더 많은 곳일때
            if 0<=x<n and 0<=y<n and bamboo[i][j] < bamboo[x][y]:
                # 방문했을 때 가장 긴 경로 선택
                memory[i][j] = max(memory[i][j], dfs(x, y))
        memory[i][j] += 1
    return memory[i][j]

ans = 0
# 처음으로 풀어놀 모든 위치 
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
        
print(ans)