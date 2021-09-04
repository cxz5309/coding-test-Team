n = int(input())
n_ls = sorted(list(map(int, input().split())))
m = int(input())
m_ls = list(map(int, input().split()))
answer = ['0' for i in range(m)]

for idx, target in enumerate(m_ls):
    low = 0
    high = n-1

    while low <= high:
        mid = round((low + high) / 2)
        if n_ls[mid] == target:
            answer[idx] = '1'
            break
        elif n_ls[mid] > target:
            high = mid - 1
        else:
            low = mid + 1


print(' '.join(answer))