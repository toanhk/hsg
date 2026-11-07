# ST25 - cach "tu nhien" nhung cham: Dijkstra tu MOI tru so h (N lan) roi duyet hoan vi.
# N lan Dijkstra: chi kip subtask 1-2 (N <= 1000); subtask 3 (N = 10^4) qua gio.
# Bai hoc: chay Dijkstra tu phia it dinh (K dai ly kiem tra), khong phai tu phia nhieu dinh.
import heapq
from itertools import permutations

def main():
    data = open('ST25.INP', 'rb').read().split()
    n, m, K = int(data[0]), int(data[1]), int(data[2])
    x = [int(v) for v in data[3:3 + K]]
    adj = [[] for _ in range(n + 1)]
    pos = 3 + K
    for _ in range(m):
        u, v, w = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = float('inf')

    def dijkstra(s):
        dist = [INF] * (n + 1); dist[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > dist[u]:
                continue
            for v, w in adj[u]:
                if du + w < dist[v]:
                    dist[v] = du + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    dx = {s: dijkstra(s) for s in set(x)}
    best, bh = INF, -1
    for h in range(1, n + 1):
        if h in dx:
            continue
        dh = dijkstra(h)
        for p in permutations(x):
            s = dh[p[0]] + dh[p[-1]]
            for i in range(K - 1):
                s += dx[p[i]][p[i + 1]]
            if s < best:
                best, bh = s, h
    with open('ST25.OUT', 'w') as f:
        f.write(f'{bh} {best}\n')

main()
