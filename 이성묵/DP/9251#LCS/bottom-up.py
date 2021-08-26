def solution_A(A, B):
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(A)][len(B)]


s1 = "ABC"
s2 = "CAVBVC"


def solution_B(A, B):
    dp = [0] * 1001
    a, b = len(A), len(B)

    for i in range(a):
        t = 0
        for j in range(b):
            if t < dp[j]:
                t = dp[j]
            elif A[i] == B[j]:
                dp[j] = t + 1
    return max(dp)


print(solution_A(s1, s2))
