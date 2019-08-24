n = int(input())

k = 2 * n -1
for i in range(0, n):
    print(" " * (k-n-i) +  "*" * (2*i+1))
for i in range(1, n):
    print(" " * i + "*" * (k - 2 * i))