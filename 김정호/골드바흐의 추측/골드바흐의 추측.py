import sys

def prime_search():
    _prime = [False, False] + [True] * (1000001 - 2)

    for i in range(2, int(1000001 ** 0.5) + 1):
        if _prime[i]:
            for j in range(i * i, 1000001, i):
                _prime[j] = False

    return _prime


prime = prime_search()

while True:
    target = int(sys.stdin.readline())
    if target == 0:
        break

    for i in range(3, target // 2 + 1):
        if prime[i] and prime[target - i]:
            print(target, '=', i, '+', target - i)
            break
    else:
        print("Goldbach's conjecture is wrong.")
