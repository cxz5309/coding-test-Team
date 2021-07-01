# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1158
   
   난이도 : __실버 5__
   
##요점
- `queue` 를 통한 풀이법
    - `순환적인 queue`를 만들기 위해 `queue.append(queue.popleft())` 를 이용

## 풀이
1. `k -1`번 만큼 `queue[0]`를 맨 뒤로 보내준다.
    ```
    try:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        result.append(queue.popleft())
    except:
        break
      ```
      - `try - except`는 `for문` 동작 중 __queue 가 비어있을 경우__ 에 대한 예외 처리