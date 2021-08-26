from bisect import bisect_left as bs


def solution(n, arr):
    lis = [arr[0]]
    trace = [0]

    for i in range(1, n):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
            trace.append(len(lis) - 1)
        else:
            idx = bs(lis, arr[i])  # 자리에 찾아서 삽입
            lis[idx] = arr[i]
            trace.append(idx)

    # 수열 복구
    res = []
    p = len(lis) - 1
    for i, j in enumerate(reversed(trace)):
        if p < 0:
            break
        if j == p:
            res.append(arr[n - 1 - i])
            p -= 1

    return res[::-1]


if __name__ == '__main__':
    r = solution(int(input()), list(map(int, input().split())))
    print(len(r))
    print(*r)