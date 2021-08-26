import sys
input = sys.stdin.readline


def solution(arr, n, m):
    for i in range(n):
        for j in range(m):
            mx = 0
            if i > 0:
                mx = arr[i - 1][j]
            if j > 0:
                mx = max(mx, arr[i][j - 1])
            arr[i][j] += mx

    return arr[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(solution(a, n, m))

