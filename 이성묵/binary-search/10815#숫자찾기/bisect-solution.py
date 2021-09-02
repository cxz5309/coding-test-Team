import bisect


def solution():
    i = lambda: list(map(int, input().split()))
    n = int(input())
    a = i()
    a.sort()
    m = int(input())
    tl = i()
    r = []
    for t in tl:
        k = bisect.bisect_left(a, t)
        if k < n and a[k] == t:
            r.append("0")
        else:
            r.append("1")
    print(*r)


if __name__ == '__main__':
    solution()
