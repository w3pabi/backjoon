n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = b.copy()
a.sort(reverse=True)
tmp.sort()

res = 0
for i in range(0, n):
    res += int(a[i]) * int(tmp[i])

print(res)