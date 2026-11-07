# CAYCON: cay n dinh (danh so 1..n), goc la dinh 1. Voi moi dinh u, in so dinh cua cay con goc u
# (gom chinh u va moi dinh "ben duoi" u). n <= 2*10^5.
# KHONG de quy: (1) BFS tu goc lay thu tu "cha truoc con" + mang cha; (2) duyet NGUOC thu tu do,
# moi dinh cong kich thuoc cua minh vao cha. Khi den luot u thi moi con cua u da xong (vi con dung sau u).
# O(n). Do: ~0,31 s voi n = 2*10^5 ca doc file (do_cay.py).
def main():
    data = open('CAYCON.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    it = map(int, data[1:2 * n - 1])
    for u, v in zip(it, it):
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1); par[1] = -1
    order = [1]                                # list lam hang doi: vong for chay tiep khi append
    for u in order:
        pu = par[u]
        for v in adj[u]:
            if v != pu:
                par[v] = u; order.append(v)
    sz = [1] * (n + 1)
    for u in reversed(order):                  # la truoc, goc sau cung
        p = par[u]
        if p > 0:
            sz[p] += sz[u]
    with open('CAYCON.OUT', 'w') as f:
        f.write(' '.join(map(str, sz[1:])) + '\n')

main()
