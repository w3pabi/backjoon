sm = list(input())

word = sm.count(' ') + 1
if sm[0] == ' ' : word -= 1
if sm[len(sm)-1] == ' ' : word -= 1

print(word)