# 동적 프로그래밍 (Bottomup)

X = int(input())
dp = [0 for _ in range(X+1)] # 값을 기억할 DP테이블

for i in range(2, X+1): # 1은 이미 1이기 때문에 계산 필요 X -> 2부터 시작
    # -1 연산의 경우 (단순 빼기는 모든 수에 적용가능, 전 값의 최소 연산에 -1 연산 횟수만 추가하면 됨)
    dp[i] = dp[i-1] + 1 # +1은 빼기 연산 횟수 의미 
    # 나눗셈이 가능한 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # +1은 %3 횟수 추가
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # +1은 %2 횟수 추가

print(dp[X])