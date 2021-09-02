n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))
sol = []


def search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return None


for i in range(m):
    result = search(arr, arr2[i], 0, n-1)
    if result == None:
        sol.append(0)
    else:
        sol.append(1)

for i in sol:
    print(i, end=" ")
