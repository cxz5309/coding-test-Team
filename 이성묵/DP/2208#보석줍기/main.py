import sys

input = sys.stdin.readline


def solution(n, m, a):
    dp = [0] * (n + 1)
    for i in range(n - 1, m - 1, -1):  # i번째 부터 선택할수 있는 부분배열의 합중 최대 값 테이블채우기
        dp[i] = max(dp[i + 1] + a[i], a[i], 0)

    r = [0]
    p = sum(a[:m])
    i = m
    while i < n:
        r.append(p + dp[i])
        p += a[i] - a[i - m]  # 길이 m 부분배열의 합
        i += 1

    return max(r)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    print(solution(n, k, a))

n, m = 8, 4
a = [-1, -1, 1, 1, 1, 1, -1, 2]
print(solution(n, m, a))
