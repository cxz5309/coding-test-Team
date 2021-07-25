a = int(input())
queue = []
for j in range(a):
    qu = input().split()
    if qu[0] == "push":
        queue.append(qu[1])
    elif qu[0] == "pop":
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif qu[0] == "size":
        print(len(queue))
    elif qu[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif qu[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif qu[0] == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
