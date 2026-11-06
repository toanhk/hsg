# HAIROBOT: bang n x n, o >= 0 la so vang, o -1 la da. Hai robot cung xuat phat o (1,1) va cung di
# den (n,n), moi buoc XUONG hoac PHAI, khong vao o da. Vang o moi o chi nhat duoc mot lan (robot nao
# den truoc lay). Tong vang lon nhat hai robot nhat duoc? Khong co duong thi in -1. n <= 100
# Y chinh: cho hai robot di DONG THOI. Sau s buoc, robot o hang r thi o cot s - r.
#   Trang thai : f[s][r1][r2] = vang lon nhat khi sau s buoc robot 1 o hang r1, robot 2 o hang r2
#                (chi xet r1 <= r2: doi ten hai robot khong doi ket qua)
#   Truy hoi   : f[s][r1][r2] = vang(o1) + vang(o2) (tru 1 lan neu r1 = r2: cung mot o)
#                + max 4 kieu buoc truoc: (r1, r2), (r1-1, r2), (r1, r2-1), (r1-1, r2-1) o buoc s-1
#   Khoi tao   : f[0][0][0] = a[0][0]
#   Thu tu     : s tang dan
#   Dap an     : f[2n-2][n-1][n-1]
# So trang thai ~ (2n) * n^2 / 2 = n^3 = 10^6 voi n = 100, moi trang thai 4 phep so sanh.
def main():
    data = open('HAIROBOT.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    AM = -1
    if a[0][0] < 0:
        f = [[AM]]
    else:
        f = [[a[0][0]]]                           # buoc 0: chi co hang 0
    lo_cu = 0
    for s in range(1, 2 * n - 1):
        lo = max(0, s - n + 1)                    # hang nho nhat hop le o buoc s
        hi = min(s, n - 1)
        # bang moi: g[r1 - lo][r2 - lo]; bang cu f danh so tu lo_cu
        k = hi - lo + 1
        g = [[AM] * k for _ in range(k)]
        kc = len(f)
        for r1 in range(lo, hi + 1):
            v1 = a[r1][s - r1]
            if v1 < 0:
                continue
            gr = g[r1 - lo]
            i0 = r1 - lo_cu                       # chi so cua r1 (giu nguyen hang) trong bang cu
            i1 = i0 - 1                           # r1 - 1 (robot 1 vua di xuong)
            f0 = f[i0] if 0 <= i0 < kc else None
            f1 = f[i1] if 0 <= i1 < kc else None
            for r2 in range(r1, hi + 1):
                v2 = a[r2][s - r2]
                if v2 < 0:
                    continue
                j0 = r2 - lo_cu
                j1 = j0 - 1
                b = AM
                if f0 is not None:
                    if 0 <= j0 < kc and f0[j0] > b: b = f0[j0]
                    if 0 <= j1 < kc and f0[j1] > b: b = f0[j1]
                if f1 is not None:
                    if 0 <= j0 < kc and f1[j0] > b: b = f1[j0]
                    if 0 <= j1 < kc and f1[j1] > b: b = f1[j1]
                if b < 0:
                    continue
                gr[r2 - lo] = b + v1 + (v2 if r2 != r1 else 0)
        f = g
        lo_cu = lo
    with open('HAIROBOT.OUT', 'w') as fo:
        fo.write(str(f[-1][-1]) + '\n')

main()
