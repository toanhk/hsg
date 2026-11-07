# DUONGDAI - ban SAI: khoi tao f = [0] * (n + 1) "cho gon", quen danh dau dinh chua toi duoc.
# Khi do f[v] thanh "duong dai nhat ket thuc o v, BAT DAU O DAU CUNG DUOC": mot duong xuat phat tu dinh
# khac 1 (khong toi duoc tu 1) van duoc tinh, va n khong toi duoc van in ra mot so thay vi KHONG.
# Ngoai ra voi trong so am, f[v] = 0 (duong rong) con lon hon moi duong that -> sai ca khi n toi duoc.
# Test bat loi: n khong toi duoc tu 1; moi trong so am; dinh nguon khac 1 co duong dai den n.
def main():
    data = list(map(int, open('DUONGDAI.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w)); deg[v] += 1
    f = [0] * (n + 1)                         # SAI
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        for v, w in adj[u]:
            if f[u] + w > f[v]:
                f[v] = f[u] + w
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('DUONGDAI.OUT', 'w') as fo:
        fo.write(str(f[n]) + '\n')

main()
