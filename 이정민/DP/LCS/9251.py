# 참고 : https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

a = input()
b = input()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        # 두 문자열 비교
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:# 이전의 최대 공통 부분수열을 계속해서 유지하기 위함
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
                    
print(max(map(max, dp)))