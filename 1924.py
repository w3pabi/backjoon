x, y = map(int, input().split())

res = ['SUN','MON','TUE','WED','THU','FRI','SAT']
days2017 = [31,28,31,30,31,30,31,31,30,31,30,31]
days=0

for i in range(1, x):
    days += days2017[i-1]

days += y
print(res[days % 7])