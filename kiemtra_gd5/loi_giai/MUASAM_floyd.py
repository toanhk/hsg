# MUASAM - ban Floyd + QHD bitmask: DUNG, du cho subtask 2 (n <= 100), nhung Floyd O(n^3) voi n = 10^4 la 10^12
# -> khong the. Bai hoc: chi can khoang cach giua cac nut QUAN TRONG (1, n, cua hang) -> s+1 lan Dijkstra.
def main():
    data = open('MUASAM.INP', 'rb').read().split()
    n, m, k, s = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][i] = 0
    p = 4
    for _ in range(m):
        u, v, w = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for t in range(1, n + 1):
        dt = d[t]
        for i in range(1, n + 1):
            dit = d[i][t]
            if dit == INF:
                continue
            di = d[i]
            for j, x in enumerate(dt):
                if dit + x < di[j]:
                    di[j] = dit + x
    nut, mon = [], []
    for _ in range(s):
        x, t = int(data[p]), int(data[p + 1]); p += 2
        mk = 0
        for y in data[p:p + t]:
            mk |= 1 << (int(y) - 1)
        p += t
        nut.append(x); mon.append(mk)
    K = 1 << k
    f = [[INF] * s for _ in range(K)]
    for j in range(s):
        f[mon[j]][j] = min(f[mon[j]][j], d[1][nut[j]])
    for mask in range(1, K):
        for j in range(s):
            if f[mask][j] == INF:
                continue
            for t in range(s):
                if mon[t] & ~mask:
                    nm = mask | mon[t]
                    f[nm][t] = min(f[nm][t], f[mask][j] + d[nut[j]][nut[t]])
    best = min(f[K - 1][j] + d[nut[j]][n] for j in range(s))
    with open('MUASAM.OUT', 'w') as fo:
        fo.write(str(best if best < INF else -1) + '\n')

main()
