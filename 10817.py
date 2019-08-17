a, b, c = map(int, input().split())

if a==b==c : print(a)
elif a==b : print(a)
elif b==c : print(b)
elif a==c : print(a)
elif c<a<b or b<a<c : print(a)
elif a<b<c or c<b<a : print(b)
elif a<c<b or b<c<a : print(c)
