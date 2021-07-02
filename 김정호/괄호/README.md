# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/9012
   
   난이도 : __실버 4__
   
##요점
- `stack`을 활용한 문제 풀이
    ![KakaoTalk_20210701_152959484](https://user-images.githubusercontent.com/84619866/124076586-6bd9bc00-da81-11eb-91d9-c30a7f1ecf64.jpg)



## 풀이
1. `len(string)`의 길이가 홀수 일 경우, 가지치기를 실행
    ```
    if len(string) % 2 != 0:  # 결코 짝이 맞을 수 없음.
      ```

2. `stack.top`과 `s`가 짝이 맞을 경우 `stack.pop()`을 하여 짝제거
    ```
    if stack and stack[-1] == '(' and s == '):
        stack.pop()
    ```
    - 이 때, `stack`이 비어있지 않을때만 동작해야한다. 안그러면 `stack.pop()`에 대한 `IndexError` 발생