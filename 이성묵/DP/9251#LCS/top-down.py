import sys

sys.setrecursionlimit(2 ** 12)


def solution(A, B):
    cache = [[-1 for _ in range(len(B))] for _ in range(len(A))]

    def lcs(i, j):
        if i == 0 or j == 0:
            return 0

        if cache[i - 1][j - 1] != -1:
            return cache[i - 1][j - 1]

        if A[i - 1] == B[j - 1]:
            cache[i - 1][j - 1] = lcs(i - 1, j - 1) + 1
        else:
            cache[i - 1][j - 1] = max(lcs(i - 1, j), lcs(i, j - 1))

        return cache[i - 1][j - 1]

    return lcs(len(A), len(B))

'''

## 접근

연속하지 않은 부분 수열이 포함 되기 때문에 모든 경우의 수를 다 구해 보아야 한다.

예를 들어 'ABA' 와 'AZA' 의 공통 수열을 재귀적으로 찾아보자

마지막 문자부터 비교를 시작하면 하나의 문자가 일치한다.

문자가 일치한다면 이런 식이 성립한다.

ABA
AZA

$L('ABA', 'AZA') = 1 + L ('AB', 'AZ')$


'' Base condition

문자가 일치 하지 않는 다면 모든 경우에 대해서 최대값을 비교한다

L('AB', 'AZ') = max (L('AB', 'A'), L('A', 'AZ'))


max(dp[i - 1][j], dp[i][j - 1])
'''

if __name__ == '__main__':
    print(solution(input(), input()))

s1 = "ACAYKP"
s2 = "CAPCAK"

print(solution(s1, s2))
