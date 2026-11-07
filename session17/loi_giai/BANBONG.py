# BANBONG: n qua bong xep hang, qua thu i ghi so a[i]. Ban vo qua i duoc a[trai] * a[i] * a[phai] diem, voi
# trai/phai la qua bong CON LAI gan nhat hai ben (khong co thi tinh la 1). Ban het; tong diem lon nhat?
# n <= 200, a[i] <= 100.
# Mau chot: chon qua bong bi ban CUOI CUNG trong doan (khong phai dau tien!). Them hai qua "1" o hai dau:
# b = [1] + a + [1]. Xet doan MO (l, r): ban het cac qua l+1..r-1, hai qua l va r van con.
#   Trang thai : f[l][r] = diem lon nhat khi ban het cac qua nam GIUA l va r (0 <= l < r <= n+1)
#   Truy hoi   : qua k (l < k < r) bi ban cuoi -> luc do hang xom cua k chinh la l va r:
#                f[l][r] = max_k f[l][k] + f[k][r] + b[l] * b[k] * b[r]
#                (hai ben k doc lap vi k con dung giua cho den luc cuoi)
#   Khoi tao   : f[l][l+1] = 0 (khong co qua nao o giua)
#   Thu tu     : l giam dan, r tang dan tu l+2
#   Dap an     : f[0][n+1]
# O(n^3/6) ~ 1,4*10^6 voi n = 200 (~0,2 s).
def main():
    data = open('BANBONG.INP', 'rb').read().split()
    n = int(data[0])
    b = [1] + list(map(int, data[1:1 + n])) + [1]
    m = n + 2
    f = [[0] * m for _ in range(m)]
    for l in range(m - 3, -1, -1):
        fl = f[l]
        bl = b[l]
        for r in range(l + 2, m):
            t = bl * b[r]
            best = 0
            for k in range(l + 1, r):
                c = fl[k] + f[k][r] + t * b[k]
                if c > best:
                    best = c
            fl[r] = best
    with open('BANBONG.OUT', 'w') as out:
        out.write(str(f[0][m - 1]) + '\n')

main()
