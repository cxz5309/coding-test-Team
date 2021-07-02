import sys

for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().split()
    revers_string = [s[::-1] for s in string]       # list comprehension 으로 문자열 뒤집기
    print(' '.join(revers_string))                  # join() 으로 문자열 합치기