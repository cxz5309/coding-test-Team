n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

a.insert(0, 0)

for i in range(n+1):
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

stack = []

a = a[n:0:-1]
dp = dp[n:0:-1]

# 항상 맨 오른쪽이 최장길이가 되는 듯하다.
# 오른쪽부터 돌면서 스택에 쌓는다.
tmp = int(max(dp))
for idx, d1 in enumerate(dp):
    if d1 == tmp:
        stack.append(a[idx])
        tmp -= 1

print(' '.join(map(str, stack[::-1])))