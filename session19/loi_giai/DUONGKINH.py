# DUONGKINH: cay n dinh, moi canh (u, v) dai w. Duong kinh = khoang cach LON NHAT giua hai dinh.
# n <= 2*10^5, 1 <= w <= 10^9.
# QHD tren cay (goc 1):
#   trang thai : xa[u] = duong di dai nhat tu u di XUONG (vao cay con u)
#   truy hoi   : xa[u] = max_{v con u} (xa[v] + w(u,v)); duong dai nhat "gap khuc" tai u (dinh cao nhat
#                cua duong la u) = tong HAI nhanh xuong dai nhat (nhanh thu hai co the = 0)
#   khoi tao   : xa[u] = 0 (la)
#   thu tu     : con truoc cha -> duyet nguoc thu tu BFS
#   dap an     : max_u (nhanh1[u] + nhanh2[u]) - moi duong deu co dung mot dinh cao nhat
# Cach khac (DUONGKINH_2lan.py): tim dinh xa nhat tu 1, roi dinh xa nhat tu do. O(n).
# Do: ~0,4 s voi n = 2*10^5 (may cham hon 0,6 s); ke luu tuple (v, w) cham hon ~30%.
def main():
    data = open('DUONGKINH.INP', 'rb').read().split()
    n = int(data[0])
    U = list(map(int, data[1:3 * n - 2:3]))   # cat lat: dau, cuoi, do dai canh
    V = list(map(int, data[2:3 * n - 2:3]))
    W = list(map(int, data[3:3 * n - 2:3]))
    adj = [[] for _ in range(n + 1)]
    for u, v, w in zip(U, V, W):
        adj[u].append(w << 18 | v)             # gop (w, v) vao MOT so nguyen (v < 2^18): nhanh hon tuple
        adj[v].append(w << 18 | u)
    M = (1 << 18) - 1
    par = [0] * (n + 1); par[1] = -1
    wpar = [0] * (n + 1)                       # do dai canh noi u voi cha
    order = [1]
    for u in order:
        pu = par[u]
        for x in adj[u]:
            v = x & M
            if v != pu:
                par[v] = u; wpar[v] = x >> 18; order.append(v)
    m1 = [0] * (n + 1)                         # nhanh xuong dai nhat (= xa[u])
    m2 = [0] * (n + 1)                         # nhanh xuong dai thu hai (qua con KHAC)
    best = 0
    for u in reversed(order):
        t = m1[u] + m2[u]
        if t > best:
            best = t
        p = par[u]
        if p > 0:
            d = m1[u] + wpar[u]                # nhanh cua p di qua u
            if d > m1[p]:
                m2[p] = m1[p]; m1[p] = d
            elif d > m2[p]:
                m2[p] = d
    with open('DUONGKINH.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
