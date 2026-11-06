# TUILON: cai tui 0/1 voi W, w[i] den 10^9 (khong lap bang theo khoi luong duoc),
# nhung gia tri nho: v[i] <= 500, n <= 100 -> tong gia tri <= 5*10^4.
# DOI VAI TRO: lap bang theo GIA TRI, luu khoi luong nho nhat.
#   Trang thai : g[t] = tong khoi luong NHO NHAT de dat DUNG gia tri t (INF neu khong dat duoc)
#   Truy hoi   : xet vat (w, v): g[t] = min(g[t], g[t - v] + w)   (t giam dan: 0/1)
#   Khoi tao   : g[0] = 0, g[t > 0] = INF
#   Thu tu     : vong ngoai vat, vong trong t giam tu (tong gia tri da xet) ve v
#   Dap an     : t lon nhat co g[t] <= W
# O(n * tong v) <= 5*10^6, chi duyet den tong gia tri cac vat da xet nen thuc te ~2.5*10^6 o.
def main():
    data = open('TUILON.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    INF = float('inf')
    g = [0]                                    # g mo rong dan theo tong gia tri da xet
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        g.extend([INF] * v)
        for t in range(len(g) - 1, v - 1, -1):
            x = g[t - v] + w
            if x < g[t]:
                g[t] = x
    t = len(g) - 1
    while g[t] > W:
        t -= 1
    with open('TUILON.OUT', 'w') as out:
        out.write(str(t) + '\n')

main()
