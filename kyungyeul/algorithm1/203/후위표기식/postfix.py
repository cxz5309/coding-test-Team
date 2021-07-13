a = int(input())
word = list(input())
arr = []
arr2 = []
count = 0

for i in range(a):
    arr.append(input())


for i in word:
    if i.isupper():
        arr2.append(arr[count])
        count += 1
    elif i == "+" or "-" or "*" or "/":
        arr2.append(i)

print("".join(arr2))


https://reakwon.tistory.com/62