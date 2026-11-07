# BANBONG - vet can (n <= 8): thu moi THU TU ban (n! <= 40320), mo phong bang list.
from itertools import permutations

def main():
    data = open('BANBONG.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    best = 0
    for tt in permutations(range(n)):
        con = list(range(n))                   # chi so cac qua con lai, theo thu tu
        diem = 0
        for i in tt:
            j = con.index(i)
            trai = a[con[j - 1]] if j > 0 else 1
            phai = a[con[j + 1]] if j + 1 < len(con) else 1
            diem += trai * a[i] * phai
            con.pop(j)
        if diem > best:
            best = diem
    with open('BANBONG.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
