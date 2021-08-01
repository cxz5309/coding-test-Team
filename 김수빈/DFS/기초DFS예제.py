# 기초 dfs 예제

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색, 단 큐가 빌(False)때 까지
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


dfs(graph, 1, visited)