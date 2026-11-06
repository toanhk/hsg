# DUONGDI - vet can: quay lui thu moi duong di (phai/xuong), lay tong lon nhat.
# So duong = C(m+n-2, m-1): m = n = 10 -> 48 620 duong; m = n = 15 -> 4*10^7 -> qua cham. Chi subtask 1.
import sys

def main():
    data = open('DUONGDI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = [list(map(int, data[2 + i * n:2 + (i + 1) * n])) for i in range(m)]
    sys.setrecursionlimit(10000)
    best = -10**30

    def thu(i, j, tong):                      # dang dung o (i, j), tong da gom ca a[i][j]
        nonlocal best
        if i == m - 1 and j == n - 1:
            best = max(best, tong)
            return
        if i + 1 < m: thu(i + 1, j, tong + a[i + 1][j])
        if j + 1 < n: thu(i, j + 1, tong + a[i][j + 1])

    thu(0, 0, a[0][0])
    with open('DUONGDI.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
