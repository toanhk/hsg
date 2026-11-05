# CAUTHANG - vet can: quay lui thu moi day buoc, dem day nao dung tai bac n
# So day buoc ~ 1.84^n: n = 20 ~ 1.2*10^5 day, n = 30 ~ 5*10^7 -> qua cham. Chi cho subtask 1.
import sys

def main():
    data = open('CAUTHANG.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    hong = set(int(x) for x in data[2:2 + k])
    sys.setrecursionlimit(10000)
    dem = 0

    def thu(i):                         # dang dung o bac i
        nonlocal dem
        if i == n:
            dem += 1
            return
        for b in (1, 2, 3):
            j = i + b
            if j <= n and j not in hong:
                thu(j)

    thu(0)
    with open('CAUTHANG.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
