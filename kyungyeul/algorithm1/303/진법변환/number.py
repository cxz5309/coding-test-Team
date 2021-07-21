a, b = input().split(" ")
b = int(b)
result, count = 0, 0
for i in a[::-1]:
    print(i)
    if i.isdigit():
        c = int(i)
        result += (c * (b ** count))
        count += 1
    else:
        c = ord(i)-55
        result += (c * (b ** count))
        count += 1
print(result)
