# QUATRAM - vet can: Floyd O(n^3) cho n <= 100, roi thu ca hai thu tu ghe tram.
def main():
    data = list(map(int, open('QUATRAM.INP', 'rb').read().split()))
    n, m, a, b = data[0], data[1], data[2], data[3]
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][i] = 0
    for i in range(m):
        u, v, w = data[4 + 3 * i], data[5 + 3 * i], data[6 + 3 * i]
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    kq = min(d[1][a] + d[a][b] + d[b][n], d[1][b] + d[b][a] + d[a][n])
    with open('QUATRAM.OUT', 'w') as f:
        f.write((str(kq) if kq < INF else '-1') + '\n')

main()
