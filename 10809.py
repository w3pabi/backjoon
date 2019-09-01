a = list(input())
b = [-1] * 26

for i in range(0, len(a)):
    point = ord(a[i]) - ord('a')
    if b[point] == -1 : b[point] = i
    else : continue
res = ""
for i in range(0, len(b)-1):
    res += str(b[i]) + " "
res += str(b[len(b)-1])

print(res)