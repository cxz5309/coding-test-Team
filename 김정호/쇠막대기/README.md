# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/10799
   
   난이도 : __실버 3__
   
##요점
- `()` 를 기준으로 `queue`의 길이만큼 막대가 나뉘어진다.
- `(` 만 단독으로 나올 경우, __새로운 막대__ 가 추가되었다는 의미
- `)` 는 한개의 막대의 끝을 표현한다. 이 때, __막대의 갯수는 1개가 증가__ 하지만 `queue`의 길이는 1 이 줄어든다

![KakaoTalk_20210702_172405133](https://user-images.githubusercontent.com/84619866/124245037-8a5fb600-db5a-11eb-9bdf-a3781a8cc57c.jpg)


## 풀이
1. `()` 를 특정 단어 `a` 로 치환
    - `string = deque(sys.stdin.readline().rstrip().replace('()', 'a'))`

2. `a` 가 나올 시, 저장된 `stack`의 길이만큼 `stick`에 더해준다.
    ```
    if stack[-1] == 'a':
        stack.pop()
        stick += len(stack)
     ```

3. `)` 가 나올 시, 막대의 끝을 알리는 것이며 막대기의 수 1개 추가
    ```        
    elif string[0] == ')':
        stack.pop()
        string.popleft()
        stick += 1
      ```