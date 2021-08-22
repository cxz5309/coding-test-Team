cache = {0: 0, 1: 1, 2: 1, 3: 1}


def solve(n):
    if n in cache:
        return cache[n]

    i = solve(n // 2) + (n % 2) + 1
    j = solve(n // 3) + (n % 3) + 1

    cache[n] = min(i, j)
    return cache[n]


if __name__ == '__main__':
    print(solve(int(input())))
