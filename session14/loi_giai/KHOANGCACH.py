# KHOANGCACH: n thanh pho, m con duong HAI CHIEU (co the nhieu duong giua 2 thanh pho), q cau hoi
# "khoang cach ngan nhat tu u den v?" (-1 neu khong toi duoc). n <= 200, m <= 2*10^4, q <= 10^5.
# Floyd: d[i][j] = duong ngan nhat i -> j chi di qua cac dinh trung gian trong {0..k}.
#   Truy hoi : d[i][j] = min(d[i][j], d[i][k] + d[k][j])     (them dinh k vao tap duoc phep di qua)
#   Thu tu   : k o VONG NGOAI CUNG (dat k vao trong la sai - xem KHOANGCACH_sai.py)
#   n^3 = 8*10^6 lan so sanh: sat moc Python -> toi uu vong trong:
#     lay hang di = d[i], dk = d[k] va dik = di[k] ra bien cuc bo; bo qua hang co dik = INF;
#     duyet enumerate(dk) thay vi range + chi so 2 chieu.  (do: 0,45 s -> 0,30 s, xem do_duongdi.py)
def main():
    data = list(map(int, open('KHOANGCACH.INP', 'rb').read().split()))
    n, m, q = data[0], data[1], data[2]
    INF = 10**18                           # so nguyen lon (khong dung float de cong nhanh, so sanh deu)
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    p = 3
    for _ in range(m):
        u = data[p] - 1; v = data[p + 1] - 1; w = data[p + 2]; p += 3
        if w < d[u][v]:                    # nhieu duong giua 2 thanh pho: giu duong re nhat
            d[u][v] = d[v][u] = w
    for k in range(n):
        dk = d[k]
        for di in d:
            dik = di[k]
            if dik == INF:                 # i khong toi duoc k: hang i khong doi
                continue
            for j, x in enumerate(dk):
                if dik + x < di[j]:
                    di[j] = dik + x
    out = []
    it = iter(data[p:p + 2 * q])
    for u, v in zip(it, it):
        x = d[u - 1][v - 1]
        out.append(str(x) if x < INF else '-1')
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
