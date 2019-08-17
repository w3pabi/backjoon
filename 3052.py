a=list()

for i in range(0,10):
    n = int(input())% 42
    if(n in a): continue
    else: a.append(n)

print(len(a))