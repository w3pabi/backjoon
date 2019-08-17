n = input()
num = n
cnt = 0

if int(num) < 10: num = "0" + num
n=num
while 1 :
    num1 = num[0]
    num2 = num[1]
    res = str(int(num1)+int(num2))
    if(len(res)==1): num = num2 + res[0]
    else: num = num2 + res[1]
    cnt+=1
    if(num==n) : break;

print(cnt)