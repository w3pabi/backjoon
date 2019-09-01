a, b = map(str, input().split())

tmp_a = ''.join(reversed(a))
tmp_b = ''.join(reversed(b))

if int(tmp_a) > int(tmp_b) : print(tmp_a)
else : print(tmp_b)