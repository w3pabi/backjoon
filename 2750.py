n = int(input())
a = [0 for i in range(n)]
for i in range(0,n):
    a[i] = int(input())

a.sort()
for i in range(0,n):
    print(a[i])