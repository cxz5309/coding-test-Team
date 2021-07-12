# 최대공약수와 최소공배수의 문제와 겹치므로 따로 README.md는 작성하지 않았다.

from math import gcd
import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    GCD = gcd(a, b)
    print(a * b // GCD)