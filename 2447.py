def shape(n):
    return "***" * n

def shape2():
    return '* *'

li = list()
for i in range(1,8):
    li.append(3**i)

n = int(input())
k = li.index(n)+1

for i in range(0,n) :
    for j in range(0, n):
        print(shape1() * j)