# dp를 계산하기 위해서 a[0]~a[i-1]을 다 훑는 방식
n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
a.insert(0, 0)

for i in range(n+1):
    if i == 0:
        dp[0] = 0
    else:
        for j in range(i-1, -1, -1):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] +1)
                
print(max(dp))