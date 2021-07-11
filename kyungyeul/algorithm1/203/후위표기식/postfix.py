a = int(input())
word = list(input())
arr = []
arr2 = []


for i in range(a):
    arr.append(input())


for i in range(len(word)):
    if word[i].isupper():
        arr2.append("대문")
    else:
        arr2.append("a")


print(arr2)
