def hanoicnt(n, from_pos, to_pos, aux_pos):
    global cnt
    if n == 1:
        cnt+=1
        return
    hanoicnt(n - 1, from_pos, aux_pos, to_pos)
    cnt+=1
    hanoicnt(n - 1, aux_pos, to_pos, from_pos)

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

n = int(input())
cnt=0
hanoicnt(n,1,3,2)
print(cnt)
hanoi(n,1,3,2)
