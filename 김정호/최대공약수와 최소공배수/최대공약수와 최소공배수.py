from math import gcd

a, b = map(int, input().split())
GCD = gcd(a, b)
print(GCD)
print(a * b // GCD)