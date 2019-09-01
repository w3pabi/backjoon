a = list(input().upper())

totalTime = 0
for i in range(0, len(a)):

    if a[i] >= 'W' : daiN = 9
    elif a[i] >= 'T' : daiN = 8
    elif a[i] >= 'P' : daiN = 7
    elif a[i] >= 'M' : daiN = 6
    elif a[i] >= 'J' : daiN = 5
    elif a[i] >= 'G' : daiN = 4
    elif a[i] >= 'D' : daiN = 3
    else : daiN = 2
    totalTime += 1 + daiN

print(totalTime)