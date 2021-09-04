def solution(n, m, a):
    cache = {}

    def dp(start: int):
        if start == n - 1:
            return a[-1]
        if start >= n:
            return 0
        if start not in cache:
            cache[start] = max(a[start], a[start] + dp(start + 1), 0)
        return cache[start]

    r = []
    p = sum(a[:m])
    i = m
    while 1:
        r.append(max(p, dp(i) + p))
        if i >= n: break
        p += a[i] - a[i - m]
        i += 1

    return max(r)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    print(solution(n, m, a))

n, m = 8, 4
a = [-1, -1, 1, 1, 1, 1, -1, 2]

# a = [1, 2, -1, -2]
# n, m = 4, 2

print(solution(n, m, a))
