t = int(input())

gword = 0

for i in range(0, t):
    a = list(input())
    b = list()
    tmp = 0

    for j in range(0, len(a)):
        if b.count(a[j])==0 :
            b.append(a[j])
            tmp = 1
        elif b.count(a[j])>0 and a[j-1]== a[j]:
            tmp =1
            continue
        elif b.count(a[j])>0 and a[j-1]!=a[j]:
            tmp=0
            break

    gword += tmp

print(gword)