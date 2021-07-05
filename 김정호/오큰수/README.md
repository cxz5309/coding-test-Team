# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/17298
   
   난이도 : __골드 4__
   
##요점
- N의 최대가 1,000,000 이므로 `O(N^2)` 으로는 시간 초과발생
- `stack` 을 활용하여 풀이하였음.
    - `stack`의 `top` 부분과 `number_list`의 요소를 반복 비교하여 오큰수 조건을 확인.
    ![KakaoTalk_20210705_175508056](https://user-images.githubusercontent.com/84619866/124445339-6e5a4f80-ddba-11eb-998a-320946a797ce.jpg)  