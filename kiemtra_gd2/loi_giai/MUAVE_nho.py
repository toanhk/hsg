# MUAVE - ban co nho (dict) + setrecursionlimit: dung nhung de quy sau n tang.
# Ket qua phu thuoc phien ban Python o phong thi:
#   - Python <= 3.11: moi tang de quy ton ngan xep C -> n ~ 10^5 da co the chet khong bao loi.
#   - Python 3.12+: khong tran nua (do tren may 3.13: 10/10 test, ~0.7 s) nhung cham gap doi ban vong lap.
# Khong nen nop ban nay: dung MUAVE.py (vong lap) cho chac.
import sys

def main():
    data = open('MUAVE.INP', 'rb').read().split()
    n = int(data[0])
    t = list(map(int, data[1:1 + n]))
    r = list(map(int, data[1 + n:n + n]))
    s = list(map(int, data[n + n:n + n + n - 2]))
    sys.setrecursionlimit(10**6)
    nho = {n: 0}

    def thu(i):
        if i in nho:
            return nho[i]
        kq = t[i] + thu(i + 1)
        if i + 1 < n: kq = min(kq, r[i] + thu(i + 2))
        if i + 2 < n: kq = min(kq, s[i] + thu(i + 3))
        nho[i] = kq
        return kq

    with open('MUAVE.OUT', 'w') as f:
        f.write(str(thu(0)) + '\n')

main()
