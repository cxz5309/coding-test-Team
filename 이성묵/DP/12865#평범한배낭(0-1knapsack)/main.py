from collections import defaultdict


def solution_1():
    n, k = map(int, input().split())
    pack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = map(int, input().split())
        for j in range(1, k + 1):
            if w <= j:
                pack[i][j] = max(
                    v + pack[i - 1][j - w],
                    pack[i - 1][j]
                )
            else:
                pack[i][j] = pack[i - 1][j]

    print(pack[-1][-1])


def solution(n, k):
    m = defaultdict(int)

    for _ in range(n):
        w, v = map(int, input().split())

        u = {}
        for gw, gv in m.items():
            nw, nv = gw + w, v + gv
            if nw <= k and nv > m[nw]:
                u[nw] = nv
        m.update(u)

    return m[k]