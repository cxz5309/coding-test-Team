# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1874
   
   난이도 : __실버 3__
   
##요점
- `queue`를 활용한 풀이
    - 그림 설명으로
    ![KakaoTalk_20210701_200335627](https://user-images.githubusercontent.com/84619866/124114460-90488f00-daa7-11eb-9108-f1a9bf294903.jpg)

## 풀이
1. `number_list`는 오름차순으로 정렬되어 있으며 __`target`보다 큰 수가 나올 때 까지__ `stack`에 저장한다.
    ```
    while number_list and number_list[0] <= target:
        stack.append(number_list.popleft())
        result.append('+')                              # + 문자 append
      ```
2. `while문` 이후 `stack[-1]`이 `target`과 일치하는 지를 확인
    ```
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
     ```

3. 결과적으로 `+`는 n개, `-`도 n개로 `len(result) == 2 * n` 이면 문제의 조건이 만족한다.
    - `if len(result) == 2 * n:`