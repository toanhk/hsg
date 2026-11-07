# QUATRAM - ban SAI: chi xet thu tu 1 -> a -> b -> n, quen thu tu 1 -> b -> a -> n.
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
    data = list(map(int, open('QUATRAM.INP', 'rb').read().split()))
    n, m, a, b = data[0], data[1], data[2], data[3]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[4:4 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    d1 = dijkstra(adj, 1, n)
    da = dijkstra(adj, a, n)
    db = dijkstra(adj, b, n)
    kq = d1[a] + da[b] + db[n]           # SAI: thieu truong hop di b truoc
    with open('QUATRAM.OUT', 'w') as f:
        f.write((str(kq) if kq < float('inf') else '-1') + '\n')

main()
