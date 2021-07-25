import math

# 입력
n, s = map(int, input().split(" "))
a = []
a = list(map(int, input().split(" ")))
arr = []

# X-D공식
for i in a:
    sol = abs(s-i)
    arr.append(sol)

# D값의 최대값 = arr 값들의 최대공약수


def gcd(arr):
    m = math.gcd(*arr)
    print(m)


gcd(arr)
