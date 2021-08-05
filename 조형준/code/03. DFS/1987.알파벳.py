import sys


# strip() 사용해서 메모리 줄임 왜인지 알아봐야 함
r, c = map(int, sys.stdin.readline().strip().split())

# 아스키코드로 문자들을 변환해서 맵에 넣음
board = [list(map(lambda x : ord(x)-65, input())) for i in range(r)]

check = [0] * 26

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def dfs(x, y, temp):
    global res

    res = max(temp, res)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 여기서 비교할 때 r, c 가 아닌 배열 길이 체크해서 써서 시간초과
        if -1 < nx < r and -1 < ny < c:
            if check[board[nx][ny]] == 0:
                check[board[nx][ny]] = 1
                dfs(nx, ny, temp + 1)
                check[board[nx][ny]] = 0


res = 1
check[board[0][0]] = 1
dfs(0, 0, res)

print(res)