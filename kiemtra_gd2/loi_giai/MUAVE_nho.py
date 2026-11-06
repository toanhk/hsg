# MUAVE - ban co nho (dict) + setrecursionlimit: dung nhung sau n tang. Qua subtask 2 (n <= 10^5)?
# Khong chac: sau 10^5 tang tren may phong co the tran ngan xep C. Subtask 3 (5*10^5) -> loi.
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
