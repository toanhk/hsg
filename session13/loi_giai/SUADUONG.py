# SUADUONG: do thi vo huong, m con duong danh so 1..m, n, m <= 5*10^4. Thanh pho chi sua cac con duong nam
# tren IT NHAT MOT duong di ngan nhat tu 1 den n. In so con duong can sua va chi so cua chung (tang dan).
# Meo HAI LAN DIJKSTRA: d1 = khoang cach tu 1, dn = khoang cach tu n (vo huong nen dn[v] = d(v, n)).
#   Duong i = (u, v, w) nam tren mot duong ngan nhat  <=>  d1[u] + w + dn[v] == D  hoac  d1[v] + w + dn[u] == D
#   voi D = d1[n]: di ngan nhat tu 1 toi u, qua canh, roi ngan nhat tu v toi n ma tong van bang D.
# Khong can liet ke duong di (co the co so mu duong ngan nhat). O((n + m) log m).
import heapq

def dijkstra(adj, s, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    data = list(map(int, open('SUADUONG.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    canh = data[2:2 + 3 * m]
    adj = [[] for _ in range(n + 1)]
    it = iter(canh)
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    d1 = dijkstra(adj, 1, n)
    dn = dijkstra(adj, n, n)
    D = d1[n]
    kq = []
    if D < float('inf'):
        for i in range(m):
            u, v, w = canh[3 * i], canh[3 * i + 1], canh[3 * i + 2]
            if d1[u] + w + dn[v] == D or d1[v] + w + dn[u] == D:
                kq.append(i + 1)
    with open('SUADUONG.OUT', 'w') as f:
        f.write(f'{len(kq)}\n' + (' '.join(map(str, kq)) + '\n' if kq else ''))

main()
