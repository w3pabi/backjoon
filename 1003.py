t = int(input())

for i in range(0,t):
    n = int(input())
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        ex_cnt0 = 1
        ex_cnt1 = 0
        cnt0 = 0
        cnt1 = 1
        for i in range(1,n):
            tmp0 = cnt1
            tmp1 = cnt0 + cnt1
            ex_cnt0 = cnt0
            ex_cnt1 = cnt1
            cnt0 = tmp0
            cnt1 = tmp1


        print(cnt0, cnt1)
