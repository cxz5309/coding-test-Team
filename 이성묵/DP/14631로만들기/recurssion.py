cache = {1: 0, 2: 1}  # 메모이제이션
# 1을 0 으로 두어야 cache[n] + 1 했을때 1이된다.


def solve(n):
    if n in cache:
        return cache[n]
    # 모듈러 연산으로 나머지 (2,3 으로 나누어 질때까지 빼주어야 하는 만큼) 더해준다
    cache[n] = min(solve(n // 2) + n % 2, solve(n // 3) + n % 3) + 1
    return cache[n]


if __name__ == '__main__':
    print(solve(int(input())))