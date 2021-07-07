n = list(input())
a = False
word = ''
result = ''
for i in n:
    if a == False:
        if i == '<':
            a = True
            word += i
        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word += i
    elif a == True:
        word = word+i
        if i == '>':
            a = False
            result += word
            word = ''

print(result+word)
