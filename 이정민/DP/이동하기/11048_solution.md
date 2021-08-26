### 11048.py 풀이법

![11048](C:%5CUsers%5CLG%5CDesktop%5Ccoding_study%5Ccoding-test-Team%5C%EC%9D%B4%EC%A0%95%EB%AF%BC%5Cimg%5C11048.jpg)

점화식

```text
dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i-1][j-1]
```

