# 진수

## 각 진수 표현법

> 2진수: 0b
> 8진수: 0o
> 16진수: 0x

## 10진수를 각 진수로 변환

> 내장함수 사용

```
a= 10
2number = bin(a) #2진수
8number = oct(a) #8진수
16number =hex(a) #16진수
결과
0b1010
0o12
0xa
```

> format사용 (cf 접두어 없애기)

```
print('{:#b}'.format(10)) #2진수
print('{:#o}'.format(10)) #8진수
print('{:#x}'.format(10)) #16진수
결과
0b1010
0o12
0xa

접두어를 없애고 싶다면?
print('{:b}'.format(10)) #2진수
print('{:o}'.format(10)) #8진수
print('{:x}'.format(10)) #16진수
결과
1010
12
a
```

## 각 진수들을 10진수로 변환

```
2number = 0b1010 #2진수
8number = 0o12   #8진수
16number =0xa    #16진수

print(2number)
print(8number)
print(16number)

or
print(int(2number,2))
print(int(8number,8))
print(int(16number,16))

int()
```
