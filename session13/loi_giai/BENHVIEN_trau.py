# BENHVIEN - vet can: Floyd O(n^3) (n <= 100) roi voi moi dinh chon cap (khoang cach, so hieu) nho nhat.
def main():
    data = list(map(int, open('BENHVIEN.INP', 'rb').read().split()))
    n, m, k = data[0], data[1], data[2]
    bv = data[3:3 + k]
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][i] = 0
    p = 3 + k
    for i in range(m):
        u, v, w = data[p + 3 * i], data[p + 3 * i + 1], data[p + 3 * i + 2]
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for t in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][t] + d[t][j] < d[i][j]:
                    d[i][j] = d[i][t] + d[t][j]
    out = []
    for v in range(1, n + 1):
        kc, h = min((d[v][h], h) for h in bv)
        out.append(f'{kc} {h}' if kc < INF else '-1')
    with open('BENHVIEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
