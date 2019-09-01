n = int(input())

k = 2 * n -1
for i in range(1,k+1):
    if i<=n : print("*" * i + " " * 2*(n-i) + "*" * i)
    else : print("*"* (k+1-i) + " " * 2*(i-n) + "*" * (k+1-i))
