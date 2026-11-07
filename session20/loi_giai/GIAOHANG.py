# GIAOHANG: n diem (diem 1 la kho). Di tu diem i den diem j mat d[i][j] phut (co the d[i][j] != d[j][i]).
# Xe xuat phat tu kho, qua MOI diem con lai DUNG mot lan roi ve kho. Thoi gian nho nhat?
# n <= 16, d[i][j] <= 10^6 (d[i][i] = 0). n = 1: dap an 0.
# Bai nguoi giao hang (TSP). Danh so diem 0..n-1, kho = 0.
#   Trang thai : f[mask][v] = thoi gian nho nhat di tu kho, qua DUNG cac diem trong mask (mask chua 0 va v),
#                hien dang dung o v.
#   Cong thuc  : f[mask][v] = min f[mask bo v][u] + d[u][v]   voi u thuoc (mask bo v).
#   Khoi tao   : f[{0}][0] = 0 (tap {0} la mask = 1).
#   Thu tu     : mask tang dan, chi xet mask LE (co kho).
#   Dap an     : min f[full][v] + d[v][0]   (nho cong duong VE kho).
# O(2^n * n^2), thuc te ~ n^2 * 2^(n-3) phep thu (mask le, u va v deu trong mask): n = 16 -> ~2*10^6, do ~0,17 s.
# n = 17 mat ~0,4 s, n = 18 ~1 s -> chi nen ra n <= 16 voi Python.
def main():
    data = open('GIAOHANG.INP', 'rb').read().split()
    n = int(data[0])
    d = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    if n == 1:
        res = 0
    else:
        INF = 10**18
        N = 1 << n
        den = [list(col) for col in zip(*d)]          # den[v][u] = d[u][v]: duyet u lien tuc theo hang
        bits = [[u for u in range(n) if m >> u & 1] for m in range(N)]   # cac bit 1 cua moi mask
        f = [None] * N
        f[1] = [0] + [INF] * (n - 1)
        for mask in range(3, N, 2):
            cur = [INF] * n
            for v in bits[mask]:
                if v == 0:
                    continue
                truoc = mask ^ (1 << v)
                p = f[truoc]
                dv = den[v]
                best = INF
                for u in bits[truoc]:                 # u = 0 chi hop le khi truoc = {0}: cac luc khac
                    x = p[u] + dv[u]                  # f[truoc][0] = INF nen tu bi loai
                    if x < best:
                        best = x
                cur[v] = best
            f[mask] = cur
        full = f[N - 1]
        res = min(full[v] + d[v][0] for v in range(1, n))
    with open('GIAOHANG.OUT', 'w') as fo:
        fo.write(str(res) + '\n')

main()
