# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/17413
   
   난이도 : __실버 3__
   
##요점
- `queue` 를 활용하여 문제 풀이
- 각 조건에 따라서 `while문` 을 추가 실행해준다.
    1. 시작문자가 `<` 일 경우 : 마지막 문자가 `>` 일 때까지 추가적인 `while문`
    2. 시작문자가 `알파벳 또는 숫자` 일 경우 : 마지막 문자가 `<` 또는 `' '` 일 때 까지 추가적인 `while`문


## 풀이
- 예제 : `<ab cd>ef gh<ij kl>`
1. 첫 시작문자가 `<` 일 경우에 대한 `while문`
    ```
    if stack[-1] == '<':                    # 첫 시작이 < 로 시작된다면 > 문자가 나올 때 까지 stack 에 append()
        while string and stack[-1] != '>':
            stack.append(string.popleft())
        reverse_result.append(''.join(stack))
      ```
      - 최종적으로 `<ab cd>` 의 문자열이 나온다. 그 문자열을 `revserse_result` 에 추가한다.

2. 첫 시작문자가 `숫자` 또는 `알파벳` 일 경우에 대한 `while문`
    ``` 
    elif stack[-1].isalnum():               # 첫시작이 숫자 또는 알파벳이면 최종적으로 뒤집어야하는 문자열
        while string and string[0] != ' ' and string[0] != '<':
            stack.append(string.popleft())
        reverse_result.append(''.join(stack[::-1]))
      ```
      - 최종적으로 `ef` 의 문자열이 나오며 이 문자는 __뒤집어져서__ 추가된다.