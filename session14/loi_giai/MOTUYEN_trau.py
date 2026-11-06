# MOTUYEN - vet can (subtask 1, n <= 50, q <= 20): them tuyen vao danh sach roi chay LAI Floyd tu dau.
# O(q * n^3) = 2,5*10^6 voi subtask 1; voi n = 200, q = 200 thi 1,6*10^9 -> khong kip.
def main():
    data = open('MOTUYEN.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    INF = 10**18
    g = [[INF] * n for _ in range(n)]
    for i in range(n):
        g[i][i] = 0
    p = 3
    for _ in range(m):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; w = int(data[p + 2]); p += 3
        g[u][v] = g[v][u] = min(g[u][v], w)
    out = []
    for _ in range(q):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; w = int(data[p + 2]); p += 3
        g[u][v] = g[v][u] = min(g[u][v], w)
        d = [r[:] for r in g]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
        out.append(str(sum(d[i][j] for i in range(n) for j in range(i + 1, n))))
    with open('MOTUYEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
