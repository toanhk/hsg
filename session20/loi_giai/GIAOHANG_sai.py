# GIAOHANG - ban SAI de chua tren lop: QHD dung nhung QUEN cong duong VE kho (lay min f[full][v]).
# Vi du in 29 thay vi 35 (thieu doan 3 -> 1 dai 6). Test n = 2 (d = 7 va 3) bat ngay: in 7 thay vi 10.
def main():
    data = open('GIAOHANG.INP', 'rb').read().split()
    n = int(data[0])
    d = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    INF = 10**18
    N = 1 << n
    f = [[INF] * n for _ in range(N)]
    f[1][0] = 0
    for mask in range(1, N, 2):
        for v in range(n):
            x = f[mask][v]
            if x == INF:
                continue
            for u in range(n):
                if not mask >> u & 1:
                    nm = mask | 1 << u
                    if x + d[v][u] < f[nm][u]:
                        f[nm][u] = x + d[v][u]
    res = min(f[N - 1])                               # SAI: thieu + d[v][0]
    with open('GIAOHANG.OUT', 'w') as fo:
        fo.write(str(res) + '\n')

main()
