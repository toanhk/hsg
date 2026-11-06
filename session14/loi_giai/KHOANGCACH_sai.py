# KHOANGCACH - BAN SAI de chua bai: dat k o VONG TRONG CUNG (for i: for j: for k). Khi tinh d[i][j],
# cac d[i][k], d[k][j] co the chua phai ngan nhat -> bo sot duong di qua nhieu dinh trung gian.
# Test bat loi: xich 1 - 3 - 2 - 4 (ten dinh xao tron), hoi 1 -> 4.
def main():
    data = open('KHOANGCACH.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    INF = 10**18
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    p = 3
    for _ in range(m):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; w = int(data[p + 2]); p += 3
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for i in range(n):
        for j in range(n):
            for k in range(n):             # SAI: k phai o vong ngoai cung
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    out = []
    for _ in range(q):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; p += 2
        out.append(str(d[u][v]) if d[u][v] < INF else '-1')
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
