# MUASAM: thanh pho n nut, m duong hai chieu (u, v, thoi gian w). Can mua du k mon (danh so 1..k). Co s cua hang,
# cua hang j o nut p[j], ban mot so mon (mua bao nhieu cung duoc, khong ton thoi gian). Xuat phat o nut 1, mua du
# k mon roi den nut n. Thoi gian nho nhat? Khong the thi in -1.
# n <= 10^4, m <= 3*10^4, w <= 10^6, k <= 10, s <= 10.
# Ket hop Dijkstra (buoi 13) + QHD bitmask (buoi 20):
#   Buoc 1: chi cac nut 1, n va cac cua hang la "quan trong". Dijkstra tu nut 1 va tu MOI cua hang (do thi vo huong
#           nen khoang cach cua hang -> n doc ngay tu Dijkstra cua cua hang): toi da s + 1 lan Dijkstra.
#   Buoc 2: QHD tren (tap mon da co, cua hang dang dung):
#     Trang thai : f[mask][j] = thoi gian nho nhat de dang o cua hang j va da mua du cac mon trong mask.
#     Cong thuc  : tu f[mask][j] di sang cua hang t (chi khi t ban mon MOI): f[mask | mon[t]][t] = f[mask][j] + D[j][t].
#                  (Ghe cua hang khong ban mon moi la thua: D la khoang cach ngan nhat, ghe hay khong cung vay.)
#     Khoi tao   : f[mon[j]][j] = d1[p[j]].
#     Thu tu     : mask tang dan (mask | mon[t] > mask).
#     Dap an     : min f[2^k - 1][j] + D[j][n].
# O((s+1) (n + m) log m + 2^k s^2). Do: ~0,26 s voi n = 10^4, m = 3*10^4, s = 10 (11 lan Dijkstra).
import heapq

def dijkstra(n, adj, s):
    INF = 1 << 62
    d = [INF] * (n + 1)
    d[s] = 0
    pq = [s]                                    # heap so nguyen d * 2^14 + u (u <= 10^4 < 2^14)
    pop, push = heapq.heappop, heapq.heappush
    while pq:
        x = pop(pq)
        du = x >> 14; u = x & 16383
        if du > d[u]:
            continue
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]:
                d[v] = nd
                push(pq, nd << 14 | v)
    return d

def main():
    data = open('MUASAM.INP', 'rb').read().split()
    n, m, k, s = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    p = 4
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
        adj[u].append((v, w)); adj[v].append((u, w))
    nut, mon = [], []
    for _ in range(s):
        x, t = int(data[p]), int(data[p + 1]); p += 2
        mk = 0
        for y in data[p:p + t]:
            mk |= 1 << (int(y) - 1)
        p += t
        nut.append(x); mon.append(mk)
    INF = 1 << 62
    full = (1 << k) - 1
    tat_ca = 0
    for mk in mon:
        tat_ca |= mk
    res = -1
    if tat_ca == full:
        d1 = dijkstra(n, adj, 1)
        bang = {}                               # nut -> mang khoang cach (hai cua hang cung nut: chay 1 lan)
        for x in nut:
            if x not in bang:
                bang[x] = dijkstra(n, adj, x)
        D = [[bang[nut[j]][nut[t]] for t in range(s)] for j in range(s)]
        den_n = [bang[nut[j]][n] for j in range(s)]
        K = 1 << k
        f = [[INF] * s for _ in range(K)]
        for j in range(s):
            if d1[nut[j]] < f[mon[j]][j]:
                f[mon[j]][j] = d1[nut[j]]
        for mask in range(1, K):
            row = f[mask]
            for j in range(s):
                x = row[j]
                if x >= INF:
                    continue
                Dj = D[j]
                for t in range(s):
                    mt = mon[t]
                    if mt & ~mask:              # cua hang t co mon chua mua
                        nm = mask | mt
                        y = x + Dj[t]
                        if y < f[nm][t]:
                            f[nm][t] = y
        best = min(f[full][j] + den_n[j] for j in range(s))
        if best < INF:
            res = best
    with open('MUASAM.OUT', 'w') as fo:
        fo.write(str(res) + '\n')

main()
