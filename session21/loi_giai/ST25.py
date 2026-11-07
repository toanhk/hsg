# ST25 (Ninh Binh 2023-2024, ngay 06/10/2023, bai 3, 6 diem) - Dijkstra + duyet hoan vi (bitmask nho)
# N dai ly, M duong hai chieu do dai w, K dai ly can kiem tra (K <= 5). Chon tru so h KHONG thuoc K dai ly,
# di tu h qua ca K dai ly roi QUAY VE h (vi du: 4 -> 1 -> 2 -> 3 -> 4 = 7), tong quang duong nho nhat.
# Nhieu h cung toi uu -> h nho nhat.  N <= 10^4, M <= 5*10^4, w <= 10^3.
# Mo hinh hoa:
#   1) Dijkstra tu moi dai ly kiem tra x[0..K-1] -> d[i][v] (K lan, khong phai N lan!).
#   2) giua[a][b] = do dai ngan nhat di qua ca K dai ly, bat dau o x[a], ket thuc o x[b]:
#      duyet K! <= 120 hoan vi, dung d[i][x[j]] lam khoang cach giua hai dai ly.
#   3) Voi moi h: chi phi = min_{a,b} d[a][h] + giua[a][b] + d[b][h]  -> K*K = 25 phep / dinh.
# Do phuc tap: K * M log N (~0,2 s) + K! * K + N * K^2. Ca bai do ~0,3 s.
# Bay: quen quay ve (sai vi du), chon h trung voi dai ly kiem tra, K = 1 (a = b, giua = 0).
import heapq
from itertools import permutations

def main():
    data = open('ST25.INP', 'rb').read().split()
    n, m, K = int(data[0]), int(data[1]), int(data[2])
    x = [int(v) for v in data[3:3 + K]]
    adj = [[] for _ in range(n + 1)]
    pos = 3 + K
    for _ in range(m):
        u, v, w = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = float('inf')
    d = []
    for s in x:                                    # K lan Dijkstra
        dist = [INF] * (n + 1); dist[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > dist[u]:
                continue                           # cap loi thoi
            for v, w in adj[u]:
                nd = du + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        d.append(dist)
    # giua[a][b]: di qua tat ca K diem, dau x[a], cuoi x[b]
    giua = [[INF] * K for _ in range(K)]
    for p in permutations(range(K)):
        s = 0
        for i in range(K - 1):
            s += d[p[i]][x[p[i + 1]]]
        if s < giua[p[0]][p[-1]]:
            giua[p[0]][p[-1]] = s
    cap = [(a, b, giua[a][b]) for a in range(K) for b in range(K) if giua[a][b] < INF]
    kiem = set(x)
    best, bh = INF, -1
    for h in range(1, n + 1):
        if h in kiem:
            continue
        c = INF
        for a, b, g in cap:
            v = d[a][h] + g + d[b][h]
            if v < c:
                c = v
        if c < best:                               # dau < : giu h nho nhat khi bang nhau
            best, bh = c, h
    with open('ST25.OUT', 'w') as f:
        f.write(f'{bh} {best}\n')

main()
