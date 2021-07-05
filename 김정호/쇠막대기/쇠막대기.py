from collections import deque
import sys

string = deque(sys.stdin.readline().rstrip().replace('()', 'a'))    # () 는 a로 치환하였음

# (((()(()()))(())()))(()()) ---> (((a(aa))(a)a))(aa) 로 치환이된다.
# 이 때, a가 나올때 마다 저장된 stack의 길이만큼 막대기 수를 더한다.
# ) 이 나온다면 괄호지우기 알고리즘과 같이 삭제시키고 막대기의 수를 1개 추가시킨다.

stack, stick = [], 0
while string:
    if not stack:
        stack.append(string.popleft())

    try:
        if stack[-1] == 'a':
            stack.pop()
            stick += len(stack)
        elif string[0] == ')':
            stack.pop()
            string.popleft()
            stick += 1
        else:
            stack.append(string.popleft())
    except:
        break
print(stick)


## 아래 문제로 푼 후 위의 문제로 코드 길이를 줄임
"""
from collections import deque
import sys

string = deque(sys.stdin.readline().rstrip())
stack, stick = [], 0

while string:
    if not stack:
        stack.append(string.popleft())
    try:
        if stack[-1] == '(' and string[0] == ')':
            stack.pop()
            string.popleft()
            stick += len(stack)
            while string[0] != '(':
                stack.pop()
                string.popleft()
                stick += 1
        else:
            stack.append(string.popleft())
    except:
        break
print(stick)
"""