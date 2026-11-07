# MIENPHI - vet can (subtask 1, n <= 100, m <= 200): thu mien phi TUNG tuyen (gia tam thoi = 0),
# moi lan chay Dijkstra O(n^2) khong heap. Tong O(m * n^2) = 2*10^6.
def main():
    data = open('MIENPHI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [tuple(int(x) for x in data[2 + 3 * i: 5 + 3 * i]) for i in range(m)]
    INF = float('inf')

    def dijkstra_n2(mien):
        g = [[INF] * (n + 1) for _ in range(n + 1)]
        for i, (u, v, w) in enumerate(canh):
            if i == mien:
                w = 0
            if w < g[u][v]:
                g[u][v] = g[v][u] = w
        d = [INF] * (n + 1); d[1] = 0
        xong = [False] * (n + 1)
        for _ in range(n):
            u = min((x for x in range(1, n + 1) if not xong[x]), key=lambda x: d[x])
            if d[u] == INF:
                break
            xong[u] = True
            for v in range(1, n + 1):
                if d[u] + g[u][v] < d[v]:
                    d[v] = d[u] + g[u][v]
        return d[n]

    kq = min([dijkstra_n2(-1)] + [dijkstra_n2(i) for i in range(m)])
    with open('MIENPHI.OUT', 'w') as f:
        f.write(str(kq if kq < INF else -1) + '\n')

main()
