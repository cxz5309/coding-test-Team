import sys

a = sys.stdin.readline().strip()

result = 0
stack = []

for i in range(len(a)):
    if a[i] == "(":
        stack.append("(")
    else:
        if a[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)
