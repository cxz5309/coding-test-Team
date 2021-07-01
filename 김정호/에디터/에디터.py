# queue를 황용한 풀이

from collections import deque
import sys

string = list(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    try:
        if command[0] == 'L':
            queue.appendleft(string.pop())
        elif command[0] == 'D':
            string.append(queue.popleft())
        elif command[0] == 'B':
            string.pop()
        else:
            string.append(command[1])
    except:
        continue
print(''.join(string) + ''.join(queue))