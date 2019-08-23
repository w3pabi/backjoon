n, k = map(int, input().split())

def factorial(a):
    res = 1
    for i in range(1, a+1):
        res *= i
    return res

if k< 0 : print("0:")
elif k > n : print("0")
else :
    res = int(factorial(n) / (factorial(k) * factorial(n-k)))
    print(res)