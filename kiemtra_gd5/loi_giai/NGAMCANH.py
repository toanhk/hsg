# NGAMCANH: n dia diem, m con duong hai chieu (u, v, thoi gian w >= 1); dia diem i co diem ngam canh b[i].
# Di tu 1 den n theo MOT duong NHANH NHAT; trong cac duong nhanh nhat chon duong co tong diem ngam canh (cac dia diem
# di qua, ke ca 1 va n) LON NHAT. In thoi gian va tong diem do; khong toi duoc n thi in -1.
# n, m <= 10^5, w, b[i] <= 10^9.
# Ket hop Dijkstra (buoi 13) + QHD tren DAG (buoi 18):
#   Cac canh u -> v nam tren duong ngan nhat (d[u] + w == d[v]) tao thanh mot DAG (w >= 1 nen d tang ngat).
#   Thu tu lay ra khoi heap cua Dijkstra (d khong giam) chinh la mot thu tu to-po cua DAG nay.
#   Trang thai : g[v] = tong diem lon nhat tren mot duong ngan nhat 1 -> v.
#   Cong thuc  : khi lay u ra (d[u] da chot), voi canh u - v:  d[u]+w < d[v]  -> d[v] moi, g[v] = g[u] + b[v];
#                                                             d[u]+w == d[v] -> g[v] = max(g[v], g[u] + b[v]).
#   Khoi tao   : d[1] = 0, g[1] = b[1].        Dap an : d[n], g[n].
# O((n + m) log m). Do: ~0,35 s voi n = m = 10^5 (m = 2*10^5 da mat ~0,65 s -> de chi cho m <= 10^5).
import heapq

def main():
    data = open('NGAMCANH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    b = [0] + list(map(int, data[2:2 + n]))
    p = 2 + n
    U = list(map(int, data[p:p + 3 * m:3]))
    V = list(map(int, data[p + 1:p + 3 * m:3]))
    W = list(map(int, data[p + 2:p + 3 * m:3]))
    adj = [[] for _ in range(n + 1)]
    for u, v, w in zip(U, V, W):
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = 1 << 62
    d = [INF] * (n + 1)
    g = [0] * (n + 1)
    d[1] = 0; g[1] = b[1]
    pq = [1]                                    # heap so nguyen d * 2^17 + u (nhanh hon tuple)
    pop, push = heapq.heappop, heapq.heappush
    while pq:
        x = pop(pq)
        du = x >> 17; u = x & 131071
        if du > d[u]:
            continue                            # ban ghi loi thoi
        gu = g[u]
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]:
                d[v] = nd; g[v] = gu + b[v]
                push(pq, nd << 17 | v)
            elif nd == d[v] and gu + b[v] > g[v]:
                g[v] = gu + b[v]                # them mot duong ngan nhat nua toi v, dep hon
    with open('NGAMCANH.OUT', 'w') as f:
        f.write('-1\n' if d[n] == INF else f'{d[n]} {g[n]}\n')

main()
