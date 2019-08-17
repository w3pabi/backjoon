a = int(input())
b = int(input())
c = int(input())
li= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
res = str(a*b*c)

for i in range(0, len(res)):
    li[int(res[i])] += 1

for i in range(0, 10):
    print(li[i])
