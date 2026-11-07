# QUATRAM: do thi vo huong co trong so, n, m <= 5*10^4. Xe phai di tu 1 den n va ghe QUA CA HAI tram a, b
# (thu tu nao cung duoc, duoc di lai dinh/canh cu). In do dai hanh trinh ngan nhat, -1 neu khong the.
# Y tuong: hanh trinh la 3 doan ngan nhat noi nhau: 1 -> a -> b -> n hoac 1 -> b -> a -> n.
#   Do thi vo huong nen d(x, y) = d(y, x): chi can 3 lan Dijkstra tu 1, tu a, tu b.
#   Dap an = min(d1[a] + da[b] + db[n],  d1[b] + db[a] + da[n]).
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
    kq = min(d1[a] + da[b] + db[n], d1[b] + db[a] + da[n])
    with open('QUATRAM.OUT', 'w') as f:
        f.write((str(kq) if kq < float('inf') else '-1') + '\n')

main()
