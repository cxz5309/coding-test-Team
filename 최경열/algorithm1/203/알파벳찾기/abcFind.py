word = list(input())
arr = [-1 for _ in range(26)]
for i in arr:
    for j in word:
        arr[ord(j)-97] = word.index(j)

print(" ".join(map(str, arr)))
