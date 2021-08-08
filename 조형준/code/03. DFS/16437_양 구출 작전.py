from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


n = int(stdin.readline().strip())
graph = [[0, []] for _ in range(n + 1)]

for i in range(2, n + 1):
    t, a, p = stdin.readline().strip().rstrip().split()
    a, p = map(int, [a, p])

    if t == 'W':
        a *= -1

    graph[i][0] = a
    graph[p][1].append(i)


def dfs(i):
    ans = graph[i][0]
    for i in graph[i][1]:
        ans += dfs(i)

    if ans < 0:
        return 0

    else:
        return ans


print(dfs(1))