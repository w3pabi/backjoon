t = int(input())

for i in range(0, t):
    a, b = map(int, input().split())
    res= pow(a,b,10)
    if res == 0: res=10
    print(res)