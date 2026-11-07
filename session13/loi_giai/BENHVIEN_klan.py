# BENHVIEN - ban CHAM: chay Dijkstra rieng tu TUNG benh vien roi lay min. Dung, nhung O(k (n + m) log m):
# qua subtask 1-2 (k nho), qua gio o subtask 3 (k = 5000, 25 000).
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
    data = list(map(int, open('BENHVIEN.INP', 'rb').read().split()))
    n, m, k = data[0], data[1], data[2]
    bv = data[3:3 + k]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[3 + k:3 + k + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    tot = [(float('inf'), 0)] * (n + 1)
    for h in bv:
        d = dijkstra(adj, h, n)
        for v in range(1, n + 1):
            if (d[v], h) < tot[v]:
                tot[v] = (d[v], h)
    out = [f'{d} {h}' if d < float('inf') else '-1' for d, h in tot[1:]]
    with open('BENHVIEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
