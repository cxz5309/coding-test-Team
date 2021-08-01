from sys import stdin
# 순열 라이브러리 import
from itertools import combinations

n = int(stdin.readline())

# 인원 조합 능력치 점수판
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

# 멤버 번호
member = [x for x in range(n)]

# 팀이 될 수 있는 순열을 담는 리스트
team = [x for x in list(combinations(member, n // 2))]

# 능력치 차이
res = 1e9

# 능력치 계산
for t in range(len(team)):

    # 스킬팀 정해주기
    skill_team = team[t]

    # 스킬팀을 제외한 나머지는 링크팀
    link_team = tuple(set(member) - set(team[t]))

    # 스킬팀 점수 계산
    skill_p = 0
    for i in range(n // 2):
        r = skill_team[i]
        for j in skill_team:
            skill_p += arr[r][j]

    # 링크팀 점수 계산
    link_p = 0
    for i in range(n // 2):
        r = link_team[i]
        for j in link_team:
            link_p += arr[r][j]

    # 최솟값 구하기
    res = min(res, abs(skill_p - link_p))

print(res)