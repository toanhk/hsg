# MIENPHI - BAN SAI (tham lam): tim MOT duong ngan nhat tu 1 den n roi mien phi tuyen dat nhat tren
# duong do. Sai vi duong tot nhat khi co ve co the la duong KHAC: vi du 1-2 (1), 2-3 (1), 1-3 (100):
# duong ngan nhat 1-2-3 gia 2, bo tuyen dat nhat con 1; nhung di thang 1-3 va mien phi thi chi 0.
from heapq import heappush, heappop

def main():
    data = open('MIENPHI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = float('inf')
    d = [INF] * (n + 1); d[1] = 0
    cha = [0] * (n + 1); gia = [0] * (n + 1)
    h = [(0, 1)]
    while h:
        du, u = heappop(h)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; cha[v] = u; gia[v] = w; heappush(h, (d[v], v))
    if d[n] == INF:
        kq = -1
    else:
        lon, v = 0, n
        while v != 1:                      # truy vet, tim tuyen dat nhat
            lon = max(lon, gia[v]); v = cha[v]
        kq = d[n] - lon
    with open('MIENPHI.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
