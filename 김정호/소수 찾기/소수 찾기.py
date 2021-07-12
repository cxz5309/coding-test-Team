def prime_search():

    # N의 최대 수는 1000이므로 리스트의 갯수는 1001개 까지 생성해야한다.
    prime = [False, False] + [True] * 999

    for i in range(2, int(1001 ** 0.5) + 1):
        if prime[i]:                            # 소수일 때, 그 수의 배수는 모두 False 로 변환
            for j in range(i * i, 1001, i):
                prime[j] = False
    return prime

prime = prime_search()
n = int(input())
print(len([i for i in map(int, input().split()) if prime[i]]))