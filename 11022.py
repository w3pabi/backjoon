t, n = map(int, input().split())

result = ""
j=0
x = list(map(int, input().split()))

for i in range(0, t):
    if(x[i] < n):
        if(result=="") : result += str(x[i])
        else: result += " " + str(x[i])

print(result)
