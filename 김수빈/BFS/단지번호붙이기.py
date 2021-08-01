#bfs1 단지번호 붙이기
from collections import deque
n = int(input())
maps = []
for _ in range(n):
    tmp = [int(i) for i in input()]
    maps.append(tmp)

def bfs(coord,maps,visited):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    queue = deque()
    queue.append((coord))
    count = 0
    while queue:
        y,x = queue.popleft()
        #방문하지 않은 지점을 경우
        if visited[y][x] == 0:
            visited[y][x] = 1
            count += 1
            #현재 위치에서 상하좌우를 탐색하며 같은 단지의 집인지 확인한다.
            for _dir in dirs:
                new_y,new_x = y + _dir[0], x + _dir[1]
                if new_x >= 0 and new_x < n and \
                new_y >= 0 and new_y < n and visited[new_y][new_x] == 0 and maps[new_y][new_x] ==1:
                    new_coord = (new_y, new_x)
                    queue.append(new_coord)
    return count

visited = [[0 for _ in range(n)] for _ in range(n)]
count = 0
answer = []
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0 and maps[y][x] == 1:
            #단지가 총 몇개있는지
            count +=1
            coord = (y,x)
            answer.append(bfs(coord,maps,visited))
answer.sort()
print(count)
print("\n".join([str(i) for i in answer]))