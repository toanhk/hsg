# TAUHOA: n ga, m tuyen tau MOT CHIEU, n, m <= 10^5. Tuyen (u, v, c, p): tau roi ga u vao cac thoi diem
# 0, p, 2p, 3p, ... va toi ga v sau c phut. Xuat phat tu ga 1 luc 0, hoi som nhat bao gio toi ga n (-1 neu khong toi).
# Van la Dijkstra, chi doi cach tinh "khoang cach moi": dang o u luc d -> chuyen tau som nhat roi u luc
# ceil(d / p) * p = (d + p - 1) // p * p, toi v luc do + c.
# Dijkstra dung vi toi som hon o u thi khong bao gio toi v muon hon (ham thoi gian toi KHONG GIAM theo d).
import heapq

def main():
    data = list(map(int, open('TAUHOA.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 4 * m])
    for u, v, c, p in zip(it, it, it, it):
        adj[u].append((v, c, p))         # co huong: chi them chieu u -> v
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == n:
            break
        for v, c, p in adj[u]:
            nd = (d + p - 1) // p * p + c   # cho chuyen tau ke tiep roi di c phut
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    with open('TAUHOA.OUT', 'w') as f:
        f.write((str(dist[n]) if dist[n] < INF else '-1') + '\n')

main()
