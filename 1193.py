n = int(input())
end=0
i=0
while end < n :
    i+=1
    end+=i

sta = end - i
if i%2 == 0 :
    print("%d/%d" % (n-sta,i-(n-sta)+1))
else :
    print("%d/%d" % (i-(n-sta)+1,n-sta))