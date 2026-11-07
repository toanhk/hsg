# RBGAME - vet can tro choi cho n <= 20: voi moi vi tri cat, minimax tren DAY THANG (l, r, x, y) co nho.
# Khong dung nhan xet "cung cua vong" -> doc lap voi loi giai chinh, dung de doi chieu.
import sys
from functools import lru_cache

def main():
    data = open('RBGAME.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    s = data[2].decode()
    ans = 0
    for cut in range(n):
        line = s[cut:] + s[:cut]

        @lru_cache(maxsize=None)
        def thang(l, r, x, y):                     # nguoi den luot co x hat B, doi thu y; con line[l..r]
            for c in (l, r):
                nx = x + (line[c] == 'B')
                if nx == k:
                    continue                       # rut hat nay la thua ngay
                nl, nr = (l + 1, r) if c == l else (l, r - 1)
                if nl > nr or not thang(nl, nr, y, nx):
                    return True
            return False

        ans += thang(0, n - 1, 0, 0)
    with open('RBGAME.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
