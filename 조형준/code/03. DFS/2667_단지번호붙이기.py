from sys import stdin, setrecursionlimit
# 재귀함수 깊이 설정
setrecursionlimit(10 ** 6)

# 입력받기
n = int(stdin.readline())
arr, res = [], []

for _ in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))

# 동서남북 탐색 좌표
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


# 입력받은 범위 크기 내에서 활동하는지 검색
def boolean(x, y):
    if x < 0 or y < 0 or x >= len(arr) or y >= len(arr):
        return 0
    return 1


# dfs
def dfs(x, y, arr, cnt):
    if not boolean(x, y):
        return False, cnt

    if arr[x][y] == 1:
        arr[x][y] = 0
        cnt += 1
        for i in range(4):
            chk, cnt = dfs(x + dx[i], y + dy[i], arr,cnt)
        return True, cnt

    return False, cnt


for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            cnt = 0
            k, cnt = dfs(x, y, arr, cnt)
            if k:
                res.append(cnt)


print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])
