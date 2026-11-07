# CHUYENBAY: n thanh pho, m chuyen bay mot chieu u -> v gia w (1 <= w <= 10^9). Bao dam bay duoc tu 1 den n.
# In 4 so: chi phi nho nhat C; so lo trinh chi phi C (mod 10^9 + 7); trong cac lo trinh chi phi C:
# so chuyen bay IT nhat va NHIEU nhat. n, m <= 10^5.
# Mo rong DUONGRE: tren DAG duong ngan nhat lam them hai QHD min / max song song voi dem:
#   it[v] / nhieu[v] = so chuyen it nhat / nhieu nhat tren cac duong ngan nhat 1 -> v.
#   Noi long u -> v (nd = d + w):
#     nd <  dist[v]: dist = nd, cnt = cnt[u], it = it[u] + 1, nhieu = nhieu[u] + 1   (bo het cai cu)
#     nd == dist[v]: cnt += cnt[u], it = min(it, it[u] + 1), nhieu = max(nhieu, nhieu[u] + 1)
# Dung vi cung ly do voi DUONGRE (w >= 1: u chot truoc v, luc chot cac gia tri cua u da du).
# O((n + m) log m)
import heapq

P = 10**9 + 7

def main():
    data = list(map(int, open('CHUYENBAY.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it3 = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it3, it3, it3):
        adj[u].append((v, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    cnt = [0] * (n + 1)
    it = [0] * (n + 1)
    nhieu = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        cu = cnt[u] % P; iu = it[u] + 1; nu = nhieu[u] + 1
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cu; it[v] = iu; nhieu[v] = nu
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                cnt[v] += cu
                if iu < it[v]:
                    it[v] = iu
                if nu > nhieu[v]:
                    nhieu[v] = nu
    with open('CHUYENBAY.OUT', 'w') as fo:
        fo.write(f'{dist[n]} {cnt[n] % P} {it[n]} {nhieu[n]}\n')

main()
