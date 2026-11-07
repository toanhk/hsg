# KIEM THU THU VIEN: chay moi ham trong do_thi.py, qhd.py, so_hoc.py tren hang tram input ngau nhien nho
# va so voi cach vet can / cach khac. Chay truoc ngay thi de chac thu vien minh mang vao dau la DUNG.
# Chay: python kiem_thu_thu_vien.py
import random
from itertools import permutations, combinations
from do_thi import *
from qhd import *
from so_hoc import *

def do_thi_ngau_nhien(n, m, wmax=None, co_huong=False):
    canh = [(random.randint(1, n), random.randint(1, n)) for _ in range(m)]
    if wmax is not None:
        canh = [(u, v, random.randint(0 if wmax == 1 else 1, wmax)) for u, v in canh]
    return canh

def ke(n, canh, co_huong=False):
    adj = [[] for _ in range(n + 1)]
    for e in canh:
        u, v = e[0], e[1]
        x = (v, e[2]) if len(e) == 3 else v
        adj[u].append(x)
        if not co_huong:
            adj[v].append((u, e[2]) if len(e) == 3 else u)
    return adj

def kiem(ten, dk):
    if not dk:
        raise AssertionError('SAI: ' + ten)

def main():
    random.seed(2026)
    for _ in range(300):
        n = random.randint(1, 8); m = random.randint(0, 12)
        # BFS va thanh phan lien thong so voi Floyd tren trong so 1
        c1 = do_thi_ngau_nhien(n, m); adj = ke(n, c1)
        D = floyd(n, [(u, v, 1) for u, v in c1])
        dist, cha = bfs(adj, 1, n)
        kiem('bfs', all((dist[v] == -1) == (D[1][v] == float('inf')) and (dist[v] == -1 or dist[v] == D[1][v])
                        for v in range(1, n + 1)))
        for t in range(1, n + 1):
            if dist[t] >= 0:
                kiem('truy_vet', len(truy_vet(cha, 1, t)) == dist[t] + 1)
        c, nhan = thanh_phan(adj, n)
        kiem('thanh_phan', all((nhan[u] == nhan[v]) == (D[u][v] < float('inf'))
                               for u in range(1, n + 1) for v in range(1, n + 1)))
        find, union, size = make_dsu(n)
        for u, v in c1:
            union(u, v)
        kiem('dsu', all((find(u) == find(v)) == (nhan[u] == nhan[v]) for u in range(1, n + 1) for v in range(1, n + 1)))
        # hai phia: so voi thu moi cach to mau
        mau = hai_phia(adj, n)
        co = any(all((mask >> (u - 1) & 1) != (mask >> (v - 1) & 1) for u, v in c1) for mask in range(1 << n))
        kiem('hai_phia', (mau is not None) == co)
        # Dijkstra, BFS 0-1, Bellman-Ford so voi Floyd
        cw = do_thi_ngau_nhien(n, m, 9); adjw = ke(n, cw)
        Dw = floyd(n, cw)
        dk, _ = dijkstra(adjw, 1, n)
        kiem('dijkstra', all(dk[v] == Dw[1][v] for v in range(1, n + 1)))
        bf, am = bellman_ford(n, cw + [(v, u, w) for u, v, w in cw], 1)
        kiem('bellman_ford', not am and all(bf[v] == Dw[1][v] for v in range(1, n + 1)))
        c01 = do_thi_ngau_nhien(n, m, 1)
        kiem('bfs01', bfs01(ke(n, c01), 1, n)[1:] == floyd(n, c01)[1][1:])
        # Kruskal so voi thu moi tap n-1 canh
        if n <= 6 and m <= 9:
            best = None
            for tap in combinations(cw, n - 1):
                f2, u2, _ = make_dsu(n)
                if all(u2(u, v) for u, v, w in tap):
                    s = sum(w for u, v, w in tap)
                    best = s if best is None or s < best else best
            kiem('kruskal', kruskal(n, [(w, u, v) for u, v, w in cw]) == (best if n > 1 else 0))
        # to-po: thu tu hop le hoac co chu trinh (so voi thu moi hoan vi)
        if n <= 6:
            ch = [(u, v) for u, v in c1 if u != v]
            adjh = ke(n, ch, co_huong=True)
            o = topo_kahn(adjh, n)
            co_thu_tu = any(all(p.index(u) < p.index(v) for u, v in ch) for p in permutations(range(1, n + 1)))
            kiem('topo', (o is not None) == co_thu_tu)
            if o:
                kiem('topo thu tu', all(o.index(u) < o.index(v) for u, v in ch))
        # QHD
        a = [random.randint(0, 6) for _ in range(random.randint(0, 9))]
        kiem('lis', lis(a) == max([len(c) for r in range(len(a) + 1) for c in combinations(a, r)
                                   if all(c[i] < c[i + 1] for i in range(len(c) - 1))]))
        do_vat = [(random.randint(1, 6), random.randint(1, 9)) for _ in range(random.randint(0, 7))]
        W = random.randint(0, 15)
        kiem('tui01', tui01(W, do_vat) == max(sum(v for w, v in c) for r in range(len(do_vat) + 1)
                                              for c in combinations(do_vat, r) if sum(w for w, v in c) <= W))
        kiem('tui_vo_han', tui_vo_han(W, do_vat) == tui01(W, [x for x in do_vat for _ in range(15)]))
        s = ''.join(random.choice('ab') for _ in range(random.randint(0, 6)))
        t = ''.join(random.choice('ab') for _ in range(random.randint(0, 6)))
        kiem('lcs', lcs(s, t) == max(r for r in range(len(s) + 1) for c in combinations(s, r)
                                     if any(''.join(c) == ''.join(d) for d in combinations(t, r))))
        kiem('sua_xau', sua_xau(s, t) >= abs(len(s) - len(t)) and sua_xau(s, t) <= max(len(s), len(t))
             and (sua_xau(s, t) == 0) == (s == t))
        if 1 <= len(a) <= 6:
            def gop_trau(b):
                if len(b) == 1:
                    return 0
                return min(gop_trau(b[:i] + [b[i] + b[i + 1]] + b[i + 2:]) + b[i] + b[i + 1] for i in range(len(b) - 1))
            kiem('gop_da', gop_da(a) == gop_trau(a))
        k = random.randint(1, 6)
        d = [[0 if i == j else random.randint(1, 9) for j in range(k)] for i in range(k)]
        kiem('tsp', tsp(d) == min(sum(d[p[i]][p[i + 1]] for i in range(len(p) - 1)) + d[p[-1]][0] + d[0][p[0]]
                                  for p in permutations(range(1, k))) if k > 1 else tsp(d) == 0)
    # so hoc
    nt = sang(1000)
    kiem('sang', all(nt[x] == (x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))) for x in range(1001)))
    C = bang_to_hop(50)
    from math import comb
    kiem("to_hop", all(C(n, k) == comb(n, k) % MOD for n in range(51) for k in range(52)) and C(5, -1) == 0)
    kiem('bcnn', bcnn(12, 18) == 36)
    # BFS luoi so voi BFS thuong
    g = [bytes(random.choice(b'..#') for _ in range(7)) for _ in range(5)]
    g[0] = b'.' + g[0][1:]
    dist, W = bfs_luoi(g, 5, 7, [(0, 0)])
    kiem('bfs_luoi', dist[W + 1] == 0)
    print('Tat ca ham trong thu vien deu qua kiem thu.')

main()
