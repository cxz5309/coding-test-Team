word = input()
arr = []


def ROT(x):
    for i in x:
        if i.isupper():
            if ord(i) <= 77:
                a = ord(i)+13
                arr.append(chr(a))
            else:
                a = ord(i)-13
                arr.append(chr(a))
        elif i.islower():
            if ord(i) <= 109:
                a = ord(i)+13
                arr.append(chr(a))
            else:
                a = ord(i)-13
                arr.append(chr(a))
        elif i.isdigit():
            arr.append(i)
        elif i.isspace():
            arr.append(i)


ROT(word)
print("".join(arr))
