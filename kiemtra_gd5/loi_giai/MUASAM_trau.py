# MUASAM - vet can (n <= 100, s <= 6): Floyd lay khoang cach moi cap, roi thu moi THU TU ghe mot tap cua hang
# (moi hoan vi cua moi tap con), tap nao mua du k mon thi tinh thoi gian 1 -> ... -> n.
from itertools import permutations

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
            for j in range(1, n + 1):
                if dit + dt[j] < di[j]:
                    di[j] = dit + dt[j]
    nut, mon = [], []
    for _ in range(s):
        x, t = int(data[p]), int(data[p + 1]); p += 2
        mon.append({int(y) for y in data[p:p + t]}); p += t
        nut.append(x)
    best = INF
    for chon in range(1, 1 << s):
        ds = [j for j in range(s) if chon >> j & 1]
        if len(set().union(*(mon[j] for j in ds))) < k:
            continue
        for thu_tu in permutations(ds):
            t = d[1][nut[thu_tu[0]]] + d[nut[thu_tu[-1]]][n]
            for a, b in zip(thu_tu, thu_tu[1:]):
                t += d[nut[a]][nut[b]]
            best = min(best, t)
    with open('MUASAM.OUT', 'w') as f:
        f.write(str(best if best < INF else -1) + '\n')

main()
