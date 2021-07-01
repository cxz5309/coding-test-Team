from collections import deque
import sys

queue = deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    try:
        if command[0] == 'push_front':
            queue.appendleft(command[1])
        elif command[0] == 'push_back':
            queue.append(command[1])
        elif command[0] == 'pop_front':
            print(queue.popleft())
        elif command[0] =='pop_back':
            print(queue.pop())
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            print(queue[0])
        elif command[0] == 'back':
            print(queue[-1])
    except:
        print(-1)