a = int(input())
word = input()
arr = []
stack = []
for i in range(a):
    arr.append(int(input()))

for i in word:
    if i.isupper():
        stack.append(arr[ord(i)-ord('A')])
    else:
        x = stack.pop()
        y = stack.pop()
        if i == "+":
            stack.append(y+x)
        elif i == "-":
            stack.append(y-x)
        elif i == "*":
            stack.append(y*x)
        elif i == "/":
            stack.append(y/x)
print("{0:.2f}".format(stack[0]))
