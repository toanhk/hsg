# BALO: n do vat, vat i nang w[i], gia tri v[i]; balo chiu toi da W. Moi vat lay hoac khong.
# Tong gia tri lon nhat? n <= 100, v[i] <= 500, w[i] va W <= 10^9
# W toi 10^9 nen KHONG lap bang theo khoi luong duoc. Nhung tong gia tri <= 100 * 500 = 5*10^4:
# doi vai -> lap bang theo GIA TRI.
#   Trang thai : g[x] = tong khoi luong NHO NHAT de chon duoc mot tap vat co tong gia tri dung x
#   Truy hoi   : xet vat (w, v): g[x] = min(g[x], g[x - v] + w), x duyet GIAM (moi vat dung 1 lan)
#   Khoi tao   : g[0] = 0, g[x > 0] = vo cung
#   Thu tu     : tung vat; trong moi vat x giam dan
#   Dap an     : x lon nhat ma g[x] <= W
# Chi duyet x den tong gia tri cac vat da xet (tong_v) -> trung binh nua bang, ~1.3*10^6 o.
def main():
    data = open('BALO.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    INF = 10**19
    tong_v = sum(int(data[3 + 2 * i]) for i in range(n))
    g = [0] + [INF] * tong_v
    tong = 0
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        tong += v
        for x in range(tong, v - 1, -1):
            y = g[x - v] + w
            if y < g[x]:
                g[x] = y
    ans = 0
    for x in range(tong_v, -1, -1):
        if g[x] <= W:
            ans = x
            break
    with open('BALO.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
