from sys import stdin


def plus_s(idx):
    for i in range(1, (idx//2) + 1):
        if res[-i:] == res[-2*i:-i]:
            return -1

    if idx == n:
        for i in range(n):
            print(res[i], end='')

        return 0

    for i in range(1, 4):
        res.append(i)

        if plus_s(idx + 1) == 0:
            return 0

        res.pop()


n = int(stdin.readline())
res = []
plus_s(0)