# MOTUYEN: n thanh pho, m con duong HAI CHIEU (ban dau lien thong). Lan luot mo q tuyen moi (u, v, w).
# Sau MOI lan mo, in tong khoang cach ngan nhat cua moi cap thanh pho (i < j). n <= 200, q <= 200.
# Chay lai Floyd sau moi tuyen: q * n^3 = 1,6*10^9 -> qua cham. Cap nhat O(n^2) moi tuyen:
#   duong moi tot hon chi co the di qua tuyen (u, v) MOT lan, theo 1 trong 2 chieu:
#   d'[i][j] = min(d[i][j],  d[i][u] + w + d[v][j],  d[i][v] + w + d[u][j])
#   Dung hang CU cua u va v (sao chep truoc khi sua). Neu w >= d[u][v] thi khong gi thay doi.
#   Cat tia theo hang: neu d[i][u] + w >= d[i][v] thi moi j: d[i][u] + w + d[v][j] >= d[i][v] + d[v][j]
#   >= d[i][j] -> nhanh "qua u roi v" vo ich; tuong tu cho "qua v roi u". Moi hang xet <= 1 nhanh.
def main():
    data = list(map(int, open('MOTUYEN.INP', 'rb').read().split()))
    n, m, q = data[0], data[1], data[2]
    INF = 10**18
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    p = 3
    for _ in range(m):
        u = data[p] - 1; v = data[p + 1] - 1; w = data[p + 2]; p += 3
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for k in range(n):                     # Floyd mot lan cho mang duong ban dau
        dk = d[k]
        for di in d:
            dik = di[k]
            if dik == INF:
                continue
            for j, x in enumerate(dk):
                if dik + x < di[j]:
                    di[j] = dik + x
    tong = sum(map(sum, d)) // 2           # moi cap tinh 2 lan (i, j) va (j, i)
    out = []
    for _ in range(q):
        u = data[p] - 1; v = data[p + 1] - 1; w = data[p + 2]; p += 3
        if w < d[u][v]:
            du = d[u][:]; dv = d[v][:]     # hang CU cua u va v
            for di in d:
                a = di[u] + w              # i ~~> u -> v : co re hon di[v] khong?
                b = di[v] + w              # i ~~> v -> u : co re hon di[u] khong?
                if a < di[v]:              # chi 1 trong 2 dieu kien co the dung (cong lai thi 2w < 0)
                    for j, x in enumerate(dv):
                        if a + x < di[j]:
                            di[j] = a + x
                elif b < di[u]:
                    for j, x in enumerate(du):
                        if b + x < di[j]:
                            di[j] = b + x
                                           # ca hai deu sai: hang i khong doi -> bo qua ca hang
            tong = sum(map(sum, d)) // 2
        out.append(str(tong))
    with open('MOTUYEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
