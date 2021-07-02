from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
queue = deque([str(i) for i in range(1, n + 1)])

result = []
while queue:
    try:
        for _ in range(k - 1):                  # k - 1 만큼 queue[0]을 뒤로 보낸다.
            queue.append(queue.popleft())
        result.append(queue.popleft())          # k 번째의 수를 빼내온다.
    except:
        break                                   # for 문 동작 중 queue.popleft() 에 대한 에러 처리
print('<' + ', '.join(result) + '>')