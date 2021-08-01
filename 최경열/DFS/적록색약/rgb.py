import sys
sys.setrecursionlimit(100000)

n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(input()))


def dfs(x, y, m):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if rgb[x][y] == m and chk[x][y] == 1:
        chk[x][y] = 0
        dfs(x-1, y, m)
        dfs(x, y-1, m)
        dfs(x+1, y, m)
        dfs(x, y+1, m)
        return True
    return False


# 일반인
result = 0
chk = [[1]*n for i in range(n)]
for a in range(n):
    for b in range(n):
        if dfs(a, b, rgb[a][b]) == True:
            result += 1

# 색맹을 위한 rgb 변경
for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'
# 색맹
result2 = 0
chk = [[1]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i, j, rgb[i][j]) == True:
            result2 += 1
# 결과
print(result, result2)
