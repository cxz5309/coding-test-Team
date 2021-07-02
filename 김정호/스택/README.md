# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/10828
   
   난이도 : __실버 4__
   
##요점
- 기본적인 `stack` 문제


## 풀이
- `try - except` 를 활용하여 `stack`이 비어있을 경우에 대한 __예외 처리__ 를 실행

    ```
    try:
        if command[0] == 'push':
            stack.append(command[1])
        elif command[0] == 'pop':
            print(stack.pop())
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        else:
            print(stack[-1])
    except:
        print(-1)
     ```
     - `stack이 비어있을 경우`에 `pop` 또는 `top`에 대한 명령에 `IndexError`가 발생하므로 이에 대한 예외 처리를 따로 `if문`없이 구현