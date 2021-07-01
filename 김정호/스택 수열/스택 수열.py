from collections import deque
import sys

n = int(sys.stdin.readline())
number_list = deque([i for i in range(1, n + 1)])

stack, result = [], []
for _ in range(n):
    target = int(sys.stdin.readline())
    while number_list and number_list[0] <= target:
        stack.append(number_list.popleft())
        result.append('+')

    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')

if len(result) == 2 * n:
    for i in result:
        print(i)
else:
    print("NO")
