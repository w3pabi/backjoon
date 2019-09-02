l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0 : tmp_1 = a // c
else : tmp_1 = (a // c) + 1

if b % d == 0 : tmp_2 = b // d
else : tmp_2 = (b // d) + 1

print(l-max(tmp_1,tmp_2))