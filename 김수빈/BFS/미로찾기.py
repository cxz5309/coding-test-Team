#bfs2 미로찾기

from collections import deque

a,b = map(int,input().split())
dist = [[0 for _ in range(b)] for _ in range(a)]

arr = []
for i in range(a):
    k = [int(i) for i in input()]
    arr.append(k)
queue = deque()
queue.append((0,0))

dist[0][0] = 1

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    cur_y, cur_x = queue.popleft()
    arr[cur_y][cur_x] = 0
    for i in range(4):
        nxt_y, nxt_x = cur_y + dirs[i][0], cur_x + dirs[i][1]
        if 0 <= nxt_y < len(arr) and 0<= nxt_x < len(arr[0]) and arr[nxt_y][nxt_x] ==1:
            queue.append((nxt_y,nxt_x))
            dist[nxt_y][nxt_x] = dist[cur_y][cur_x] + 1
            arr[nxt_y][nxt_x] = 0

print(dist[a-1][b-1])