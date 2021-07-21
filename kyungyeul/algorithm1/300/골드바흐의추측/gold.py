a = int(input())
arr = []


def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


for i in range(1, a+1):
    if isPrime(i):
        arr.append(i)

x = len(arr)
for i in range(x):
    for j in range(i+1, x):
        if arr[i]+arr[j] == a:
            print(a, "=", arr[i], "+", arr[j])
