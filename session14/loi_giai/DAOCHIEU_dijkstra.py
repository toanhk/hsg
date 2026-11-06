# DAOCHIEU - Dijkstra voi heapq tren cung do thi 0/1: van DUNG, nhung cham hon BFS 0-1 khoang 2 lan
# (moi lan noi long ton mot heappush O(log)). Dung de so sanh thoi gian voi DAOCHIEU.py.
from heapq import heappush, heappop

def main():
    data = open('DAOCHIEU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append((v, 0)); adj[v].append((u, 1))
    INF = m + 1
    d = [INF] * (n + 1); d[1] = 0
    h = [(0, 1)]
    while h:
        du, u = heappop(h)
        if du > d[u]:
            continue                       # ban ghi loi thoi
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heappush(h, (d[v], v))
    with open('DAOCHIEU.OUT', 'w') as f:
        f.write(str(d[n] if d[n] < INF else -1) + '\n')

main()
