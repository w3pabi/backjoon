
a = list(input().upper())
b = [0] * 26

for i in range(0, len(a)):
    point = ord(a[i]) - ord('A')
    b[point] += 1

if b.count(max(b))>1 :
    print('?')
else :
    res = ord('A') + b.index(max(b))
    print(chr(res))