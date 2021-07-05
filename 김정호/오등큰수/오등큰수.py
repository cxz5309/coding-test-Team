# 오큰수 문제에서 '비교 대상이 등장횟수'로 바뀐 것뿐이다.
# 즉 Counter 를 활용해 등장횟수를 해쉬로 저장하여 불러오는 작업만 추가될뿐 크게 달라지는 로직은 전혀없음.

from collections import Counter
import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
number_counter = Counter(number_list)
stack, result = [], [-1] * n

for i, value in enumerate(number_list):
    while stack and number_counter[stack[-1][1]] < number_counter[value]:       # 달라진 부분
        _i, _value = stack.pop()
        result[_i] = value
    stack.append([i,  value])

for i in result:
    print(i, end=' ')