from itertools import combinations

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(" "))))

team = []
members = [i for i in range(n)]
gap = 10000
# 조합을 사용하여 스타트,링크팀 가능한 경우 생성
for i in list(combinations(members, n//2)):
    team.append(i)

for i in range(len(team)//2):
    # 스타트팀
    team_AB = team[i]
    stat_A = 0
    for j in range(n//2):
        # x인덱스(member)
        member = team_AB[j]
        # y 인덱스(k)
        for k in team_AB:
            # x,y좌표의 스탯
            stat_A += arr[member][k]
    # 링크팀
    team_AB = team[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team_AB[j]
        for k in team_AB:
            stat_B += arr[member][k]
    gap = min(gap, abs(stat_A-stat_B))
print(gap)
