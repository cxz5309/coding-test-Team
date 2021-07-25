import sys


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0


def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]


n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == "push":
        push(commend[1])
    elif commend[0] == "pop":
        print(pop())
    elif commend[0] == "size":
        print(size())
    elif commend[0] == "empty":
        print(empty())
    elif commend[0] == "top":
        print(top())
