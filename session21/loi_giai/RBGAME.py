# RBGAME (Ninh Binh 2023-2024, ngay 07/10/2023, bai 2, 7 diem) - bai ve nha buoi 21 - QHD tren doan + tro choi
# Vong n hat R/B. Phong cat vong o mot vi tri (thanh day thang), roi hai nguoi luan phien rut 1 hat o mot
# trong hai dau; ai rut du k hat B truoc thi THUA. Dem so vi tri cat ma Phong (di truoc) chac thang.
# 1 <= k < n <= 100, k <= 30, so hat B >= 2k - 1.
# Nhan xet then chot: phan con lai luon la mot CUNG lien tiep cua vong; hat da rut = phan bu cua cung,
#   khong phu thuoc vi tri cat. Biet cung (s, L) va so hat B nguoi den luot da rut (x) thi suy ra
#   so hat B doi thu da rut: y = (tong B - B trong cung) - x.
# QHD:
#   Trang thai : thang[L][s][x] = nguoi DEN LUOT thang chac khong, khi con cung bat dau s, dai L, minh co x hat B.
#   Truy hoi   : rut hat o dau trai (s) hoac dau phai (s+L-1). Neu la B va x+1 = k -> nuoc thua, bo.
#                Con lai: doi thu den luot voi cung moi va so B cua ho la y
#                -> nuoc thang neu thang[L-1][cung moi][y] = False.
#   Khoi tao   : L = 0 khong bao gio xay ra hop le (da co nguoi du k), dat False.
#   Thu tu     : L tang dan.
#   Dap an     : vi tri cat i: Phong rut hat i (con cung (i+1, n-1)) hoac hat i-1 (con cung (i, n-1)), x = 0.
# So trang thai n * n * k = 3*10^5, moi trang thai 2 nuoc -> do ~0,25 s.
def main():
    data = open('RBGAME.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    s = data[2].decode()
    b = [1 if ch == 'B' else 0 for ch in s]
    B = sum(b)
    # xanh[L][s] = so hat B trong cung (s, L): tinh qua mang cong don tren vong nhan doi
    pre = [0] * (2 * n + 1)
    for i in range(2 * n):
        pre[i + 1] = pre[i] + b[i % n]
    truoc = [bytes(k)] * n                          # L = 0: thang = False voi moi s, x
    for L in range(1, n):
        cur = [None] * n
        for st in range(n):
            da_rut = B - (pre[st + L] - pre[st])    # so hat B ngoai cung
            trai, phai = st, (st + L - 1) % n
            bt, bp = b[trai], b[phai]
            moi_t = truoc[(st + 1) % n]             # cung sau khi rut dau trai
            moi_p = truoc[st]                       # cung sau khi rut dau phai
            row = bytearray(k)
            lo = max(0, da_rut - k + 1)             # can y = da_rut - x < k
            hi = min(k - 1, da_rut)
            for x in range(lo, hi + 1):
                y = da_rut - x
                # rut dau trai
                if not (bt and x + 1 == k) and not moi_t[y]:
                    row[x] = 1
                elif not (bp and x + 1 == k) and not moi_p[y]:
                    row[x] = 1
            cur[st] = bytes(row)
        truoc = cur
    # truoc = bang cho L = n - 1
    ans = 0
    for i in range(n):
        ok = False
        if not (b[i] and k == 1) and not truoc[(i + 1) % n][0]:
            ok = True
        j = (i - 1) % n                             # dau phai cua day cat tai i
        if not (b[j] and k == 1) and not truoc[i][0]:
            ok = True
        ans += ok
    with open('RBGAME.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
