t = int(input())
li = list()

for i in range(0,t):
    li = input()
    res = 0
    cnt = 0
    for j in range(0, len(li)):
           if(li[j]=="X"):
               cnt = 0
               res += cnt

           else:
               cnt += 1
               res += cnt
    print(res)