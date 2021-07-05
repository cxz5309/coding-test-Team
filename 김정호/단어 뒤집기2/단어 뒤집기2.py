import sys
from collections import deque

string = deque(sys.stdin.readline().rstrip())
reverse_result = []         # 최종 출력되어야 하는 문자열

while string:
    stack = []

    # 전체 while 문 1번 돌 때마다 문자열이 완성되므로 stack 을 루프마다 초기화해준다.
    if not stack:
        stack.append(string.popleft())

    if stack[-1] == '<':                    # 첫 시작이 < 로 시작된다면 > 문자가 나올 때 까지 stack 에 append()
        while string and stack[-1] != '>':
            stack.append(string.popleft())
        reverse_result.append(''.join(stack))

    elif stack[-1].isalnum():               # 첫시작이 숫자 또는 알파벳이면 최종적으로 뒤집어야하는 문자열
        while string and string[0] != ' ' and string[0] != '<':
            stack.append(string.popleft())
        reverse_result.append(''.join(stack[::-1]))

    else:                                   # 그 이외는 ' '일 뿐인데 이건 그냥 append()하여 붙여준다.
        reverse_result.append(' ')

print(''.join(reverse_result))