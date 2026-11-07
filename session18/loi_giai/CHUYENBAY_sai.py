# CHUYENBAY - ban SAI: khi tim duoc duong NGAN HON (nd < dist[v]) chi cap nhat dist va cnt, quen dat lai
# it[v], nhieu[v] - van giu min/max cua cac duong CU (dai hon). Hay gap khi them mot QHD moi vao code san:
# moi lan "reset" mot trang thai phai reset MOI mang di kem. Test bat: mot duong it chuyen nhung dat duoc
# tim thay truoc, sau do moi tim ra duong re hon nhieu chuyen.
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
    it = [INF] * (n + 1)
    nhieu = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1; it[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cnt[u]          # SAI: quen it[v], nhieu[v]
                it[v] = min(it[v], it[u] + 1); nhieu[v] = max(nhieu[v], nhieu[u] + 1)
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                cnt[v] = (cnt[v] + cnt[u]) % P
                it[v] = min(it[v], it[u] + 1); nhieu[v] = max(nhieu[v], nhieu[u] + 1)
    with open('CHUYENBAY.OUT', 'w') as fo:
        fo.write(f'{dist[n]} {cnt[n] % P} {it[n]} {nhieu[n]}\n')

main()
