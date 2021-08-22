import sys

input = sys.stdin.readline


def solution(arr, k):
    dp = [0] + [10e10] * k  # max 값으로 배열 초기화

    for c in arr:
        for i in range(c, k + 1):
            if dp[i] > dp[i - c] + 1:  # i를 만들수 있는 최소 개수 업데이트
                dp[i] = dp[i - c] + 1

    return dp[k] if dp[k] != 10e10 else -1  # k 가 업데이트 되지 않았으면 방법이 없다


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [i for i in set(map(int, sys.stdin.read().splitlines())) if i <= k]  # 중복 되는 동전과 k 보다 큰 동전 거르기
    if k in a:
        print(1)
        exit(0)
    print(solution(a, k))