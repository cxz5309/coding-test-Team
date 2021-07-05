# N의 최대 수가 1000000 이므로 O(N^2) 풀이가 아닌 O(N) 정도의 수준으로 풀이.
# O(N^2)으로 해본 결과 역시 시간초과.

import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
stack, result = [], [-1] * n

for i, value in enumerate(number_list):             # 인덱스의 번호 또한 stack에 저장하기 위함.
    while stack and stack[-1][1] < value:           # stack 이 존재하고 오큰수에 해당되는 수 일 경우
        index_info, value_info = stack.pop()
        result[index_info] = value
    stack.append([i, value])

for i in result:
    print(i, end=' ')