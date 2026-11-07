# GIOHANG (de thi thu so 3, bai 2, 7 diem) - cai tui theo NHOM (moi nhom chon toi da 1 mon)
# n mon hang, mon i thuoc nhom g[i], gia w[i], do hai long v[i]. Moi nhom mua TOI DA MOT mon, tong tien <= B.
# Tong do hai long lon nhat? n <= 1000, B <= 5000, 1 <= w[i] <= B, v[i] <= 10^6, g[i] <= n.
# QHD:
#   Trang thai : f[b] = do hai long lon nhat voi tong tien <= b, chi dung cac nhom da xet.
#   Cong thuc  : xet nhom G: f_moi[b] = max(f[b], max_{i thuoc G, w[i] <= b} f[b - w[i]] + v[i]).
#                Moi mon trong nhom deu cap nhat tu f CU (ban sao "truoc") -> khong bao gio lay 2 mon cung nhom.
#   Khoi tao   : f[b] = 0 voi moi b (chua mua gi).
#   Thu tu     : tung nhom; trong nhom, tung mon (thu tu b khong quan trong vi doc tu ban sao).
#   Dap an     : f[B].
# Do phuc tap n * B = 5*10^6 o. Vong for thuan trong Python 0,4-0,75 s tuy may (GIOHANG_vonglap.py: sat gio,
# may phong thi cham hon de qua). Viet bang map(max, ...) tren lat cat: ca bai ~0,3 s.
# Bang 2 chieu dp[nhom][b] (GIOHANG_bang.py) ~1,1 s o test lon -> mat diem.
# Bay: cap nhat tai cho trong nhom (GIOHANG_sai.py), bang 2 chieu n x B (GIOHANG_bang.py, cham va ton bo nho).
def main():
    data = open('GIOHANG.INP', 'rb').read().split()
    n, B = int(data[0]), int(data[1])
    nhom = {}
    pos = 2
    for _ in range(n):
        g, w, v = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        nhom.setdefault(g, []).append((w, v))
    f = [0] * (B + 1)
    for ds in nhom.values():
        truoc = f[:]                                   # trang thai TRUOC khi xet nhom nay
        for w, v in ds:
            if w > B:
                continue
            # f[b] = max(f[b], truoc[b - w] + v) cho b = w..B, viet tren ca lat cat cho nhanh
            f[w:] = map(max, f[w:], [x + v for x in truoc[:B + 1 - w]])
    with open('GIOHANG.OUT', 'w') as fo:
        fo.write(str(f[B]) + '\n')

main()
