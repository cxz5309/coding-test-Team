import sys

for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()

    # 괄호의 갯수가 홀수이면 절대 짝이 맞을 수 없다.
    if len(string) % 2 != 0:
        print('NO')
        continue

    stack = []
    for s in string:
        if stack and stack[-1] == '(' and s == ')':     # stack 이 비어있지 않고 top 과 s가 짝이 맞을 경우, pop()
            stack.pop()
        else:                                           # stack 이 비어있거나 짝이 맞지 않을 경우, append(s)
            stack.append(s)

    # 모든 짝이 일치하다면, stack 은 비어있어야 한다..
    if stack:
        print('NO')
    else:
        print('YES')