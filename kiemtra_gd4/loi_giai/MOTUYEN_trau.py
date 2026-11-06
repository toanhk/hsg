# MOTUYEN - vet can (n <= 100): Floyd tinh khoang cach moi cap, roi voi moi de xuat chay lai Dijkstra
# "ngay tho" O(n^2) tren do thi co them tuyen do. O(n^3 + k * n^2): chi cho subtask 1.
def main():
    data = open('MOTUYEN.INP', 'rb').read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    INF = float('inf')
    g = [[INF] * (n + 1) for _ in range(n + 1)]
    p = 3
    for _ in range(m):
        u, v, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
        if w < g[u][v]:
            g[u][v] = g[v][u] = w
    de_xuat = []
    for _ in range(k):
        de_xuat.append((int(data[p]), int(data[p + 1]), int(data[p + 2]))); p += 3

    def ngan_nhat(them):
        d = [INF] * (n + 1); d[1] = 0; xong = [False] * (n + 1)
        for _ in range(n):
            u = min((x for x in range(1, n + 1) if not xong[x]), key=lambda x: d[x])
            xong[u] = True
            for v in range(1, n + 1):
                w = g[u][v]
                if them and {u, v} == {them[0], them[1]}:
                    w = min(w, them[2])
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
        return d[n]

    best = ngan_nhat(None); tuyen = 0
    for i, e in enumerate(de_xuat, 1):
        t = ngan_nhat(e)
        if t < best:
            best = t; tuyen = i
    with open('MOTUYEN.OUT', 'w') as f:
        f.write('-1\n' if best == INF else f'{best} {tuyen}\n')

main()
