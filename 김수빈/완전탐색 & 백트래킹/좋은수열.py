# 좋은 수열
n = int(input())
result = []

def checkSequence(count):
    for i in range(1,count // 2 + 1): # 체크해야되는 반복수열 개수
        if result[count - 2 * i:count - i] == result[count-i:]: #반복하는지 안하는지 체크
            return False
    return True

def backTracking(count):
    if not checkSequence(count): #좋은 수열인지 체크
        return False #좋은 수열이 아닌경우 False을 리턴
    if count == n : # 입력값 n 과 단계가 같으면 수열을 출력
        print(*result, sep='')
        return True
    for i in range(1,4):
        result.append(i) # 결과값에 추가
        if backTracking(count + 1):
            return True #
        result.pop()
backTracking(0)