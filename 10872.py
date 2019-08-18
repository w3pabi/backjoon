def f(a):
    if a==0 or a==1: return 1
    elif a>1 : return a * f(a-1)

n = int(input())

print(f(n))