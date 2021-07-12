# 에라토스테네의 체를 활용한 소수 찾기
# 이 문제의 경우 에라토스테네스를 사용하지 않으면 시간 초과

def prime_search(b):
    prime = [False, False] + [True] * (b - 2)

    for i in range(2, int(b ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, b, i):
                prime[j] = False
    return prime


a, b = map(int, input().split())
prime = prime_search(b + 1)
for i in range(a, b + 1):
    if prime[i]:
        print(i)