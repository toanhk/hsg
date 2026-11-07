# DUONGRE: do thi CO HUONG n dinh, m cung u -> v gia ve w (1 <= w <= 10^9). In chi phi nho nhat di tu 1
# den n va SO CACH di voi dung chi phi do (mod 10^9 + 7); khong toi duoc: in "-1 0". n, m <= 10^5.
# Ket hop Dijkstra + QHD dem:
#   cnt[v] = so duong ngan nhat tu 1 den v. Khi noi long cung u -> v (nd = d + w):
#     nd <  dist[v] : tim duoc duong NGAN HON -> moi cach cu bo het: cnt[v] = cnt[u]
#     nd == dist[v] : them mot nhom cach moi cung do dai  -> cnt[v] += cnt[u]
# Vi sao dung: w >= 1 nen moi dinh u dung truoc v tren duong ngan nhat (dist[u] < dist[v]) deu duoc LAY RA
# (chot) truoc v; luc u duoc lay ra thi cnt[u] da du. Cac cung dung "dong gop" chinh la cac cung cua
# DAG duong ngan nhat, Dijkstra duyet DAG do dung thu tu tang dist = mot thu tu to-po.
# Bat buoc bo cap loi thoi (d > dist[u]): neu khong u bi xu ly 2 lan, cnt[u] bi cong vao ke 2 lan (DUONGRE_sai).
# Neu cho phep w = 0 thi cach nay SAI (va so duong co the vo han) - de bai da cam.  O((n + m) log m)
import heapq

P = 10**9 + 7

def main():
    data = list(map(int, open('DUONGRE.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:                 # cap loi thoi
            continue
        cu = cnt[u] % P                 # u da chot: cnt[u] da du
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cu
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                cnt[v] += cu
    with open('DUONGRE.OUT', 'w') as fo:
        if dist[n] == INF:
            fo.write('-1 0\n')
        else:
            fo.write(f'{dist[n]} {cnt[n] % P}\n')

main()
