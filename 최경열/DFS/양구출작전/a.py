import sys
sys.setrecursionlimit(123458)
input = sys.stdin.readline

n = int(input())
# n+1의 이유는
# 노드번호가 1~N까지 시작하므로,
# 인덱스 0까지 초기화 해주기 위해서임
connect = [[] for _ in range(n + 1)]
# 0인덱스 빈배열, 시작노드1은 0,0
node = [[], [0, 0]]

# n-1은 n개의 섬에서 시작섬을 제외한 나머지
for i in range(n-1):
    animal, count, line = map(str, input().rstrip().split())
    # 노드간 관계, 즉 다리와 섬의 관계
    connect[int(line)].append(i+2)
    # 양 또는 늑대와 숫자
    node.append([animal, int(count)])


def dfs(v):
    # result는 양,result 세팅
    if node[v][0] == "W":
        result = 0
    else:
        result = node[v][1]
    if len(connect[v]) == 0:
        if node[v][0] == "S":
            return node[v][1]
        else:
            return 0
    else:
        # 섬끼리 연결된 다리가 있다면
        # 그 섬들의 양들을 계산
        for x in connect[v]:
            result += dfs(x)
    # 늑대일때 밑 노드들을 탐색후 결과반영
    if node[v][0] == "W":
        # 늑대가 더 많다면
        if result < node[v][1]:
            # 늑대는 최대1마리 양밖에 못먹음
            node[v][1] -= result
            # 양은 다 먹혔으므로 0
            result = 0
        # 양이 더 많다면
        else:
            result -= node[v][1]
            # 늑대는 최대1마리 양밖에 못먹음(다먹음)
            node[v][1] = 0
    return result


print(dfs(1))
