from sys import stdin
from itertools import combinations as comb

n = int(stdin.readline().rstrip())
arr = []
team_numbers = [x for x in range(1, n + 1)]
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

teams = list(comb(team_numbers, n // 2))
res = 1e9

for i in range(len(teams)):
    skill_team = teams[i]
    link_team = tuple(set(team_numbers) - set(skill_team))

    s_score = 0
    for j in range(n // 2):
        r = skill_team[j]
        for j in skill_team:
            s_score += arr[r - 1][j - 1]

    l_score = 0
    for j in range(n // 2):
        r = link_team[j]
        for j in link_team:
            l_score += arr[r - 1][j - 1]

    res = min(res, abs(s_score - l_score))

print(res)

