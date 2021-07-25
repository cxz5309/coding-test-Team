import sys
from collections import deque

q = deque()
stack = []
a = list(sys.stdin.readline().strip())
result = ""
state = True
for i in a:
    if i == "<":
        while stack:
            result += stack.pop()
        q.append(i)
        state = False
    elif i == ">":
        q.append(i)
        state = True
        while q:
            result += q.popleft()
    elif i == " ":
        if state:
            while stack:
                result += stack.pop()
            result += " "
        else:
            q.append(i)
    else:
        if state:
            stack.append(i)
        else:
            q.append(i)

while stack:
    result += stack.pop()

print(result)
