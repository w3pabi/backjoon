a = list(input())

tmp =len(a)
i=0
while i < len(a):
    if a[i] == '=':
        if a[i-2] =='d' and a[i-1]=='z' and i>1 :
            tmp -= 2
        elif(a[i-1]=='c' or a[i-1]=='s' or a[i-1]=='d' or a[i-1]=='z'):
            tmp -= 1
    elif a[i] == 'j' and (a[i-1] =='l' or a[i-1]=='n') :
        tmp -= 1
    elif a[i]=='-' and (a[i-1] =='d' or a[i-1]=='c'):
        tmp -= 1

    i+=1

print(tmp)