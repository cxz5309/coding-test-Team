# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/6588
   
   난이도 : __실버 1__ 
   
##요점
- `에라토스테네스의 체` 를 활용한 풀이

## 풀이
1. `for -else문` 을 활용하여 골드바흐 추측에서 벗어날 경우, `if문` 없이 `print()` 구현
    ```
    for i in range(3, target // 2 + 1):     # 3부터 시작인 이유는 문제의 조건 때문이다.
        if prime[i] and prime[target - i]:
            print(target, '=', i, '+', target - i)
            break
    else:
        print("Goldbach's conjecture is wrong.")
      ```
    - `for -else문` 은 `break` 탈출을 하지 않을 시, `else:` 문이 동작된다.

## 문제점
1. `투 포인트` 활용한 풀이 방식 또한 __시간 초과__ 발생
    - 두 소수가 되는 홀수를 찾을 때, 최악의 경우 `O(N / 2)` 가 될 수도 있음.
    #### 해결 방안
    -  `prime[i]` 가 소수일 경우, `prime[target - i]` 한개만을 확인한다.
    - 즉, target = 8 일 때, prime[3(i)] == 소수이며 prime[8(target) - 3(i)] --> prime[5] 또한 소수이므로 조건 달성
