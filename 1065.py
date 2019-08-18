n = input()
res = 0
for i in range(1, int(n)+1):
    if i<100:
        res = i
    elif i>=100 and i<1000:
      j = str(i)
      if int(j[0]) - int(j[1]) == int(j[1]) - int(j[2]): res +=1
    else : break

print(res)