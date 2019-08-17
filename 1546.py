t = int(input())
li = list(map(int, input().split()))
M =max(li)
for i in range(0,len(li)):
    li[i] = li[i] / M * 100

avg = sum(li, 0.00) / len(li)
print(avg)