from collections import deque
INF = 1e9

arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split(" "))))


# 아기상어 크기
shark_size = 2
# 아기상어 좌표
shark_x, shark_y = 0, 0


# 아기상위 위치를 나타내는 9를 찾는다
# arr의 아기상어 위치는 추후 계산시 물고기로 접근못하게 하기위해
# 0으로 초기화
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_x, shark_y = i, j
            arr[shark_x][shark_y] = 0


# 아기상어 위치를 기준으로 전체맵의 거리(최단)

def bfs():
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((shark_x, shark_y))
    dist[shark_x][shark_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 아기상어가 이동할수 있는 경우
            if dist[nx][ny] == -1 and arr[nx][ny] <= shark_size:
                dist[nx][ny] = dist[x][y]+1
                queue.append((nx, ny))
    return dist

# 최단거리가 주어줬을시, 먹을수 있는 물고기를 찾는 함수


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # dist는 아기상어 근처거리, arr는 먹을수 있는 물고기
            if dist[i][j] != -1 and 1 <= arr[i][j] and arr[i][j] < shark_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        # 가장 가까운 먹을 수 있는 물고기 좌표
        return x, y, min_dist


result = 0
ate = 0
while True:
    # 먹을 수있는 물고기 위치
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        shark_x, shark_y = value[0], value[1]
        result += value[2]
        # 먹은 물고기 위치를 0으로
        arr[shark_x][shark_y] = 0
        ate += 1
        if ate >= shark_size:
            shark_size += 1
            ate = 0
