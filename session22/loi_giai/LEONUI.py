# LEONUI (de thi thu so 2, bai 2, 7 diem) - "canh lon nhat nho nhat" tren luoi = Kruskal/DSU (buoi 16, DOCTHAP)
# Ban do m x n, o (i, j) cao h. Di 4 huong tu o (1,1) den o (m,n). Do met cua duong di = chenh lech do cao
# LON NHAT giua hai o ke lien tiep tren duong. Tim do met nho nhat. m, n <= 300, 0 <= h <= 10^6.
# Mo hinh: dinh = o, canh = hai o ke nhau, trong so = |chenh lech|. Can duong di co canh lon nhat nho nhat.
# Kruskal: xet canh theo trong so tang dan, noi bang DSU; lan dau (1,1) va (m,n) cung tap thi trong so canh
# vua noi chinh la dap an (moi canh nho hon chua du de noi hai o).
# Ma hoa canh thanh MOT so nguyen  w << SH | (o << 1 | huong)  de sap xep nhanh (buoi 16: sap so nguyen
# nhanh gap doi tuple); SH du lon de chua o << 1 | huong. O(mn log(mn)); do ~0,3 s voi 300 x 300.
def main():
    data = open('LEONUI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    h = list(map(int, data[2:2 + m * n]))       # o (i, j) -> chi so i*n + j
    if m * n == 1:
        ans = 0
    else:
        SH = (2 * m * n).bit_length()
        MASK = (1 << (SH - 1)) - 1
        canh = []
        for p in range(m * n):
            if (p + 1) % n:                      # sang phai
                canh.append(abs(h[p] - h[p + 1]) << SH | p << 1)
            if p + n < m * n:                    # xuong duoi
                canh.append(abs(h[p] - h[p + n]) << SH | p << 1 | 1)
        canh.sort()
        par = list(range(m * n))

        def find(u):                             # khong de quy, nen nua duong (buoi 15)
            while par[u] != u:
                par[u] = par[par[u]]
                u = par[u]
            return u

        s, t = 0, m * n - 1
        ans = 0
        for e in canh:
            p = (e >> 1) & MASK
            q = p + n if e & 1 else p + 1
            p, q = find(p), find(q)
            if p != q:
                par[p] = q
                if find(s) == find(t):           # vua noi duoc (1,1) voi (m,n)
                    ans = e >> SH
                    break
    with open('LEONUI.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
