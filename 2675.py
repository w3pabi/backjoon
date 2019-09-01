t = int(input())

for j in range(0, t):
    a, b = map(list, input().split())
    res = ""
    for i in range(0, len(b)):
        res +=  str(b[i]) * int(a[0])

    print(res)
