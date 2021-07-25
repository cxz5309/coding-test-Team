# 리버스

## 뒤집는 방법은 대표적으로 reverse, reversed, [::-1]이 있다.

## reverse

- list타입에서 제공하는 함수
- list에서 제공하므로 list만 가능
- 원본을 변경한다.

```
arr== ['a', 'b', 'c']
arr.reverse()

print(arr) # ['c', 'b', 'a']


```

## reversed

- 내장함수
- iterator의 요소를 역순으로 리턴
- 원본을 변경하지 않는다.
- 다시 꺼낼시 list로 변경

```
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'
s= ['abc', 'qwe'] 인덱스 순서만 바뀜
reversed(l)  # <listreverseiterator object at 0x101053c10>
reversed(t)  # <reversed object at 0x101053b50>
reversed(d)  # TypeError: argument to reversed() must be a sequence
reversed(s)  # <reversed object at 0x101053c10>
list(reversed(s)) # "cba"
list(reversed(s)) # ['qwe', 'abc']

```

## [::-1] 확장슬라이싱

```
arr3 = 'abc' 단어하나하나가 바뀜
arr3 = ['abc', 'qwe'] 인덱스 순서만 바뀜
print(arr3[::-1]) # cba
print(arr3[::-1]) # ['qwe', 'abc']

```
