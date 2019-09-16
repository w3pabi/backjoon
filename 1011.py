t = int(input())

for i in range(0, t):
    x, y =  map(int, input().split())
    r = y - x
    k = 1
    p = 1
    while r > 0:
        r -= k
        k += 1
        if r >= p:
            r -= p
            p += 1

    print(k+p-2)