# DUONGKINH - cach khac (DUNG): hai lan duyet. Tu dinh 1 tim dinh A xa nhat; tu A tim dinh B xa nhat;
# d(A, B) la duong kinh. Chi dung khi moi canh KHONG AM. Tren cay khoang cach = tong canh tren
# duong duy nhat nen chi can duyet (thu tu bat ky), cong don khoang cach tu cha.
def xa_nhat(n, adj, s):
    d = [-1] * (n + 1); d[s] = 0
    q = [s]
    for u in q:
        du = d[u]
        for v, w in adj[u]:
            if d[v] < 0:
                d[v] = du + w; q.append(v)
    t = max(range(1, n + 1), key=d.__getitem__)
    return t, d[t]

def main():
    data = open('DUONGKINH.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(1, 3 * n - 2, 3):
        u, v, w = int(data[i]), int(data[i + 1]), int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    A, _ = xa_nhat(n, adj, 1)
    B, kq = xa_nhat(n, adj, A)
    with open('DUONGKINH.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
