# XETAI: n thanh pho, m cay cau hai chieu, cau i chiu duoc xe nang toi da w. q truy van (s, L):
# xe nang L xuat phat tu s chi duoc qua cau co w >= L; dem so thanh pho xe toi duoc (ke ca s).
# n, m, q <= 10^5; w, L <= 10^9.
# XU LY OFFLINE: tra loi truy van theo L GIAM DAN. Khi L giam, tap cau qua duoc chi TANG THEM -> them cau vao
# DSU theo w giam dan (giong Kruskal cay khung lon nhat). Truoc khi tra loi truy van (s, L), them moi cau
# co w >= L; dap an = size cua thanh phan chua s. Luu dap an theo chi so goc roi in dung thu tu.
# O((m + q) log) - moi cau chi them mot lan. Do: ~0,5 s voi n = m = q = 10^5 (doc 5*10^5 so da mat 0,1 s).
def main():
    data = open('XETAI.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    U = list(map(int, data[3:3 + 3 * m:3]))
    V = list(map(int, data[4:4 + 3 * m:3]))
    W = list(map(int, data[5:5 + 3 * m:3]))
    p = 3 + 3 * m
    S = list(map(int, data[p:p + 2 * q:2]))
    L = list(map(int, data[p + 1:p + 2 * q:2]))
    cau = sorted(range(m), key=W.__getitem__, reverse=True)
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    kq = [0] * q
    j = 0                                      # cau[j] la cau tiep theo chua them
    for k in sorted(range(q), key=L.__getitem__, reverse=True):
        lk = L[k]
        while j < m and W[cau[j]] >= lk:
            i = cau[j]; j += 1
            a = U[i]
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            b = V[i]
            while parent[b] != b:
                parent[b] = parent[parent[b]]; b = parent[b]
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a; size[a] += size[b]
        x = S[k]
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        kq[k] = size[x]
    with open('XETAI.OUT', 'w') as f:
        f.write('\n'.join(map(str, kq)) + '\n')

main()
