# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1406
   
   난이도 : __실버 3__
   
##요점
- `queue`를 활용하여 풀이함.
- 알고리즘 그림 설명
    ![KakaoTalk_20210701_160949959](https://user-images.githubusercontent.com/84619866/124081782-e953fb00-da86-11eb-8b49-5e05f805e276.jpg)
    - `D`와 `B`에 관련된 명령도 비슷하게 구현 가능

## 풀이
1. `try - except`를 활용하여 예외 처리
    - `더 이상 커서가 움질일 수 없는 곳일 때`에 대한 예외 처리

2. `popleft()`를 통해 왼쪽순으로 `append()`가능
    ```
    if command[0] == 'L':
            queue.appendleft(string.pop())
      ```
    - 일반적인 append()는 뒤에 추가되지만 `appendleft()` 는 왼쪽으로 추가된다. `deque()`로 선언되었을 때만 가능.