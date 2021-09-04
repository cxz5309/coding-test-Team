n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]

dp = [10001 for _ in range(k+1)] # 값을 기억할 DP테이블, 가장 큰 값으로 채우기
dp[0] = 0 # 어느 동전으로도 채울 수 없으므로 0으로 초기화

for c in coin_list:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1) # dp[i] : 현재 자신의 값, dp[i-c]+1 : coin의 값만큼 뺀 index 값에 + 1   
        
if dp[k] == 10001: # 불가능한 경우
    print(-1)
else: 
    print(dp[k])