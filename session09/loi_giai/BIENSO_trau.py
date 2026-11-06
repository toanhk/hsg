# BIENSO - vet can: thu moi day phep bam do dai 0, 1, 2, ... (quay lui co gioi han do sau),
# dung o do dai dau tien toi duoc B. 3^d day -> chi subtask 1 (A, B <= 20, dap an <= 7).
import sys

L = 10**6

def main():
    A, B = map(int, open('BIENSO.INP', 'rb').read().split()[:2])
    sys.setrecursionlimit(10000)

    def thu(x, con):                           # con = so lan bam con duoc phep
        if x == B:
            return True
        if con == 0:
            return False
        for y in (x + 1, x - 1, 2 * x):
            if 0 <= y <= L and thu(y, con - 1):
                return True
        return False

    d = 0
    while not thu(A, d):
        d += 1
    with open('BIENSO.OUT', 'w') as f:
        f.write(str(d) + '\n')

main()
