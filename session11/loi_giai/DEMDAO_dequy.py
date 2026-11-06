# DEMDAO - DFS DE QUY "sach giao khoa" (dung cho subtask 1-2). De doc nhung nguy hiem trong Python:
# dao hinh con ran dai 5*10^5 o -> do sau de quy 5*10^5. Tren may cloud (Python 3.13, Linux) van dung
# nhung mat ~2 giay o Test09; tren Windows / Python cu de bi tran ngan xep C (chuong trinh sap) du da
# setrecursionlimit. Thu: python cham_thu.py DEMDAO loi_giai/DEMDAO_dequy.py
import sys

def main():
    data = open('DEMDAO.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = [bytearray(r) for r in data[2:2 + m]]
    sys.setrecursionlimit(10**6)

    def loang(i, j):                         # tra ve so o cua dao chua (i,j), danh dau thanh '.'
        g[i][j] = 46
        dt = 1
        for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= u < m and 0 <= v < n and g[u][v] == 35:
                dt += loang(u, v)
        return dt

    so_dao = lon_nhat = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 35:
                so_dao += 1
                lon_nhat = max(lon_nhat, loang(i, j))
    with open('DEMDAO.OUT', 'w') as f:
        f.write(f'{so_dao} {lon_nhat}\n')

main()
