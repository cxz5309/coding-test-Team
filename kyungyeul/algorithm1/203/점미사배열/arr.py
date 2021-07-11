word = input()
arr = []


def x(value):
    for i in range(len(word)):
        arr.append(word[i:len(word)])
    sort = sorted(arr)
    result2 = " ".join(sort)
    print(result2)


x(word)
