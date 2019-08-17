t = int(input())
li = list()

for i in range(0,t):
    li = input().split()
    su = 0
    for j in range(1, int(li[0])+1):
        su += int(li[j])
    avg = su / int(li[0])
    cnt = 0
    res = 0
    for j in range(1, int(li[0])+1):
        if avg < int(li[j]) : cnt += 1
    res = round(cnt / int(li[0]) * 100 , 3)
    print('%.3f' % res + "%")