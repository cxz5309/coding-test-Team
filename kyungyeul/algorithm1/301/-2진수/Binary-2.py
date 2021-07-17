N = int(input())
if not N:
    print("0")
result = ""
while N:
    if N % (-2):
        result = "1"+result
        N = N//-2+1
    else:
        result = "0"+result
        N = N//-2
print(result)
