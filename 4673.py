def d(n):
    ans = str(n)
    res = n
    for i in range (0, len(ans)):
        res += int(ans[i])
    return res


a = list()
for i in range(1, 10001):
    a.append(i)

for i in range(1, 10001):
    try:
        if a.index(d(i)) > 0 : a.remove(d(i))
    except: ValueError

for i in range(0, len(a)):
    print(a[i])