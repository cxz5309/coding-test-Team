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


if __name__ == '__main__':
    print(solution(input(), input()))

s1 = "ACAYKP"
s2 = "CAPCAK"

print(solution(s1, s2))
