# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1676
   
   난이도 : __실버 4__
   
##요점
- 펙토리얼 구하기
- `string[::-1]` 를 활용한 문자열 뒤집기

## 풀이
- `result` 를 __문자열로 치환__ 한 후 `string[::-1]` 를 활용해 뒤집은 후 `'0'` 인지를 비교
    ```
    for s in str(result)[::-1]:     # 정수를 문자열로 치환 후 문자열 뒤집기
    ```
  
- 문자열이 `0` 인지를 비교하여 `cnt` 의 수를 증가
    ```    
    if s == '0':
        cnt_0 += 1
    else:               # 0이 아닐 경우 for문 탈출
        break
     ```