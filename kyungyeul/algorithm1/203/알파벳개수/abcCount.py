word = list(input())

arr = [0 for _ in range(26)]

for i in word:
    arr[ord(i)-97] += 1

print(" ".join(map(str, arr)))
