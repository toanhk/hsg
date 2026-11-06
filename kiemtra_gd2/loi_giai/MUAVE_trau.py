# MUAVE - vet can: de quy thu nhom dau hang gom 1, 2 hoac 3 nguoi. ~1.84^n lan goi: subtask 1 (n <= 20).
import sys

def main():
    data = open('MUAVE.INP', 'rb').read().split()
    n = int(data[0])
    t = list(map(int, data[1:1 + n]))
    r = list(map(int, data[1 + n:n + n]))
    s = list(map(int, data[n + n:n + n + n - 2]))
    sys.setrecursionlimit(10000)

    def thu(i):                                  # nguoi i (dem tu 0) dang dung dau hang
        if i == n:
            return 0
        kq = t[i] + thu(i + 1)
        if i + 1 < n: kq = min(kq, r[i] + thu(i + 2))
        if i + 2 < n: kq = min(kq, s[i] + thu(i + 3))
        return kq

    with open('MUAVE.OUT', 'w') as f:
        f.write(str(thu(0)) + '\n')

main()
