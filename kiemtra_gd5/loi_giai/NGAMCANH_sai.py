# NGAMCANH - ban SAI de chua: chi cap nhat g[v] khi d[v] GIAM HAN (quen truong hop nd == d[v]),
# nen chi giu duong ngan nhat tim thay DAU TIEN chu khong phai duong dep nhat. Dung khi duong ngan nhat duy nhat.
import heapq

def main():
    data = open('NGAMCANH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    b = [0] + list(map(int, data[2:2 + n]))
    p = 2 + n
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = int(data[p + 3 * i]), int(data[p + 3 * i + 1]), int(data[p + 3 * i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = 1 << 62
    d = [INF] * (n + 1); g = [0] * (n + 1)
    d[1] = 0; g[1] = b[1]
    pq = [(0, 1)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; g[v] = g[u] + b[v]
                heapq.heappush(pq, (d[v], v))
    with open('NGAMCANH.OUT', 'w') as f:
        f.write('-1\n' if d[n] == INF else f'{d[n]} {g[n]}\n')

main()
