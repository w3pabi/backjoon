import sys

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = (x2-x1)**2 + (y2-y1)**2
    add_r = (r1+r2)**2
    sub_r = (r1-r2)**2
    if x1==x2 and y1==y2:
        if r1==r2: print(-1)
        else: print(0)
    else:
        if add_r < d : print(0)
        elif add_r == d : print(1)
        else:
            if sub_r == d : print(1)
            elif sub_r > d : print(0)
            else : print(2)