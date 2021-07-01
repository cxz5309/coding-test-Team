# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/9093
   
   난이도 : __브론즈 1__
   
##요점
- `list comprehension`을 활용하여 __pythonic한 코딩
- `' '.join()`을 활용하여 문자열 리스트를 합친다.

## 풀이
1. `revers_string = [s[::-1] for s in string]`
     - 문자열의 경우 `string[::-1]`로 쉽게 뒤집을 수 있다.
     
2. `print(' '.join(revers_string)) `
    - `''.join(string)`은 문자열로 구성된 `string`을 간편하게 하나로 합칠 수 있다.