# HONUOC - cach "ngay tho": dem tung vung nuoc (DFS de quy), vung nao khong cham mep bang thi la ho.
# Dung, nhung de quy sau -> chi an toan voi bang nho (subtask 1).
import sys

def main():
    data = open('HONUOC.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = [bytearray(r) for r in data[2:2 + m]]
    sys.setrecursionlimit(10**5)

    def loang(i, j):                         # tra ve (so o, co cham mep khong)
        g[i][j] = 35
        dt, mep = 1, i == 0 or j == 0 or i == m - 1 or j == n - 1
        for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= u < m and 0 <= v < n and g[u][v] == 46:
                a, b = loang(u, v)
                dt += a
                mep = mep or b
        return dt, mep

    so_ho = tong = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 46:
                dt, mep = loang(i, j)
                if not mep:
                    so_ho += 1
                    tong += dt
    with open('HONUOC.OUT', 'w') as f:
        f.write(f'{so_ho} {tong}\n')

main()
