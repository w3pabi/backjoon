n = int(input())
cnt = 0
tmpn = n

while True:
    if tmpn % 5 ==0:
        cnt += tmpn//5
        print(cnt)
        break
    tmpn -= 3
    cnt += 1
    if tmpn <0:
        print("-1")
        break