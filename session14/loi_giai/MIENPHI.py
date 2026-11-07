# MIENPHI: n thanh pho, m tuyen xe HAI CHIEU, tuyen u - v gia w. Ban co 1 ve mien phi, dung cho toi da
# MOT tuyen bat ky. Tim tong tien it nhat de di tu 1 den n (-1 neu khong toi duoc).
# n <= 3*10^4, m <= 6*10^4, w <= 10^9.
# Cach 1 (file nay): duong di tot nhat co dang  1 ~~> u  --(mien phi)-->  v ~~> n.
#   d1 = Dijkstra tu 1, dn = Dijkstra tu n. Dap an = min tren moi tuyen (u, v) cua
#   d1[u] + dn[v] va d1[v] + dn[u]. Hai lan Dijkstra + mot vong qua canh: O(m log m).
#   (w >= 1 nen dung ve luon khong thiet; khong can xet rieng truong hop "khong dung ve".)
# Cach 2 (MIENPHI_tang.py): do thi trang thai (dinh, da dung ve chua) - xem giao an.
from heapq import heappush, heappop

def main():
    data = list(map(int, open('MIENPHI.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    canh = list(zip(it, it, it))           # (u, v, w)
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = float('inf')

    def dijkstra(s):
        d = [INF] * (n + 1); d[s] = 0
        h = [(0, s)]
        while h:
            du, u = heappop(h)
            if du > d[u]:
                continue                   # ban ghi loi thoi
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd; heappush(h, (nd, v))
        return d

    d1 = dijkstra(1)
    dn = dijkstra(n)
    kq = d1[n]
    for u, v, w in canh:
        if d1[u] + dn[v] < kq:
            kq = d1[u] + dn[v]
        if d1[v] + dn[u] < kq:
            kq = d1[v] + dn[u]
    with open('MIENPHI.OUT', 'w') as f:
        f.write(str(kq if kq < INF else -1) + '\n')

main()
