import sys
d, n = map(int, input().split())
oven_size = list(map(int, input().split()))
dough = list(map(int, input().split()))
# if 오븐 지름이 앞 지름보다 크면 사용 불가능으로 앞지름으로 맞춰주기
# ex) 오븐이 5 6 인 경우 반죽이 6은 5를 들어갈 수 없음
# [5, 6, 4, 3, 6, 2, 3] --> [5, 5, 4, 3, 3, 2, 2]
for idx in range(d-1):
    if oven_size[idx] < oven_size[idx+1]:
        oven_size[idx+1] = oven_size[idx]
        
### 위 코드 short ver.
# for i in range(1, d):
#     oven_size[i] = min(oven_size[i], oven_size[i-1])
    
dough_idx = 0
res = 0
for i in range(d-1, -1, -1):

    if dough_idx >= len(dough):
        print(res+1)
        sys.exit()
    # 뒤에서부터 넣을 수 있는 도우 찾기
    if oven_size[i] >= dough[dough_idx]:
        dough_idx += 1
        res = i

print(0)