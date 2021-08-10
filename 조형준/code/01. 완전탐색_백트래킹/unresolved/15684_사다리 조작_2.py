from sys import stdin

n, m, h = map(int, stdin.readline().rstrip().split())
arr = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    arr[a - 1][b - 1] = 1


def move():
    for i in range(n):
        num = i
        for j in range(h):
            if arr[j][num]:
                num += 1
            elif arr[j][num - 1]:
                num -= 1
        if num != i:
            return 0
    return 1


def dfs(cnt, idx, r):
    global res

    if cnt == r:
        if move():
            res = cnt
        return

    for i in range(idx, h):
        for j in range(n - 1):
            if arr[i][j]:
                continue

            if (j + 1 <= n and arr[i][j + 1]) or (j - 1 < 0 and arr[i][j - 1]):
                continue

            arr[i][j] = 1
            dfs(cnt + 1, i, r)
            arr[i][j] = 0


res, flag = 1e9, 1

for i in range(4):
    dfs(0, 0, i)
    if res != 1e9:
        print(res)
        flag = 0
        break

if flag:
    print(-1)