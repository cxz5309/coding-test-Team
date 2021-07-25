a, b = map(int, input().split(" "))

big = max(a, b)
small = min(a, b)
while small != 0:
    big = big % small
    big, small = small, big

print(big)
print(a*b//big)
