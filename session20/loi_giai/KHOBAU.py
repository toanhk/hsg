# KHOBAU: ban do R x C, '#' la da (khong di duoc), '.' la dat trong, 'S' la cho xuat phat, '*' la kho bau
# (k kho bau). Moi phut di sang mot o chung canh. Thoi gian nho nhat de nhat HET kho bau (khong can quay ve)?
# Co kho bau khong toi duoc -> -1.   R, C <= 200, 0 <= k <= 15.
# KET HOP do thi + QHD:
#   Buoc 1 (buoi 11): BFS tren luoi tu S va tu moi kho bau -> ma tran D[i][j] = so buoc ngan nhat giua cac
#           "diem quan trong" (0 = S, 1..k = kho bau). (k+1) lan BFS, moi lan O(R*C).
#   Buoc 2 (buoi 20): TSP KHONG quay ve tren k diem:
#     Trang thai : f[mask][v] = thoi gian nho nhat di tu S, nhat DUNG cac kho bau trong mask, dang o kho bau v.
#     Cong thuc  : f[mask][v] = min f[mask bo v][u] + D[u][v], u thuoc mask bo v.
#     Khoi tao   : f[{v}][v] = D[0][v].
#     Thu tu     : mask tang dan.          Dap an : min f[full][v].
# Do phuc tap: 16 BFS x 4*10^4 o + 2^15 * 15^2 / 4 ~ 1,8*10^6 phep thu -> do ~0,4 s (test 200 x 200, k = 15).

def main():
    data = open('KHOBAU.INP', 'rb').read().split()
    R, C = int(data[0]), int(data[1])
    W = C + 2                                         # luoi co VIEN da bao quanh: khong can kiem tra bien
    o = bytearray(b'#' * ((R + 2) * W))
    diem = [0]                                        # diem[0] = S, sau do la cac kho bau
    for i in range(R):
        dong = data[2 + i]
        o[(i + 1) * W + 1:(i + 1) * W + 1 + C] = dong
        for j in range(C):
            ch = dong[j]
            if ch == 83:                              # 'S'
                diem[0] = (i + 1) * W + j + 1
            elif ch == 42:                            # '*'
                diem.append((i + 1) * W + j + 1)
    k = len(diem) - 1
    huong = (1, -1, W, -W)
    D = []
    for s in diem:                                    # BFS tu moi diem quan trong
        dist = [-1] * len(o)
        dist[s] = 0
        hd = [s]                                      # list lam hang doi: "for p in hd" di tiep khi hd dai them
        for p in hd:
            dp1 = dist[p] + 1
            for h in huong:
                q = p + h
                if dist[q] < 0 and o[q] != 35:        # 35 = '#'
                    dist[q] = dp1
                    hd.append(q)
        D.append([dist[t] for t in diem])
    if k == 0:
        res = 0
    elif min(D[0]) < 0:                               # co kho bau khong toi duoc tu S
        res = -1
    else:
        INF = 10**9
        K = 1 << k
        T = [[D[u + 1][v + 1] for u in range(k)] for v in range(k)]   # T[v][u] = khoang cach u -> v
        bits = [[u for u in range(k) if m >> u & 1] for m in range(K)]
        f = [None] * K
        f[0] = [INF] * k
        for mask in range(1, K):
            cur = [INF] * k
            for v in bits[mask]:
                truoc = mask ^ (1 << v)
                if truoc == 0:
                    cur[v] = D[0][v + 1]
                    continue
                p = f[truoc]
                tv = T[v]
                best = INF
                for u in bits[truoc]:
                    x = p[u] + tv[u]
                    if x < best:
                        best = x
                cur[v] = best
            f[mask] = cur
        res = min(f[K - 1])
    with open('KHOBAU.OUT', 'w') as fo:
        fo.write(str(res) + '\n')

main()
