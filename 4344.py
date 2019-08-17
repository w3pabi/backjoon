t = int(input())
li = list()

for i in range(0,t):
    li = int(input().split())
    avg = sum(li, 0.00)
    print(str(avg) + "%")