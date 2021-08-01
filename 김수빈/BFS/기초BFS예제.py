# 기초 bfs 예제
from collections import deque

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


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색, 단 큐가 빌(False)때 까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


bfs(graph, 1, visited)