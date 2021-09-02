n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)] # 값을 기억할 DP테이블
dp[0] = 1 # 아무 동전을 선택하지 않는 경우도 하나의 경우의 수

for c in coin_list:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])       