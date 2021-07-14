a, b, c, = map(int, input().split(" "))

one = (a+b) % c
two = ((a % c) + (b % c)) % c
three = (a*b) % c
four = ((a % c) * (b % c)) % c

print(one)
print(two)
print(three)
print(four)
