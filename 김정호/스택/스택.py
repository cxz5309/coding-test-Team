import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    # try - except 을 활용하여 stack이 비어있을 경우 pop, top 에 대한 예외 처리
    try:
        if command[0] == 'push':        # 명령어가 push 일 경우
            stack.append(command[1])
        elif command[0] == 'pop':       # 명령어가 pop 일 경우
            print(stack.pop())
        elif command[0] == 'size':      # 명령어가 size 일 경우
            print(len(stack))
        elif command[0] == 'empty':     # 명령어가 empty 일 경우
            if stack:
                print(0)
            else:
                print(1)
        else:                           # 명령어가 top일 경우
            print(stack[-1])
    except:
        print(-1)