# PHANCUM: n diem nguyen (x, y). Khoang cach hai diem = |x1 - x2| + |y1 - y2| (Manhattan). Chia n diem thanh
# DUNG k nhom khac rong sao cho khoang cach NHO NHAT giua hai diem thuoc hai nhom KHAC nhau la LON NHAT.
# In gia tri do.  2 <= k <= n <= 1500; 0 <= x, y <= 10^9.
# Ket qua quen thuoc: chay Kruskal tren do thi day du, dung lai khi con DUNG k thanh phan; canh tiep theo
# noi hai thanh phan khac nhau chinh la dap an. Tuong duong: dap an = canh lon thu (k-1) cua cay khung nho nhat
# (bo k-1 canh lon nhat cua cay khung -> k nhom).
# Do thi day n(n-1)/2 ~ 1,1*10^6 canh: sinh + sap canh qua cham -> dung PRIM O(n^2) khong heap:
# moi buoc lay dinh chua vao cay co dist nho nhat, cap nhat dist cac dinh con lai. ~0,3 s voi n = 1500.
def main():
    data = open('PHANCUM.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    X = list(map(int, data[2:2 + 2 * n:2]))
    Y = list(map(int, data[3:3 + 2 * n:2]))
    INF = 1 << 62
    dist = [INF] * n                           # dist[v] = canh re nhat noi v voi cay hien tai
    vao = [False] * n
    dist[0] = 0
    canh_cay = []                              # trong so cac canh cua cay khung
    for _ in range(n):
        u = -1; best = INF
        for v in range(n):
            if not vao[v] and dist[v] < best:
                best = dist[v]; u = v
        vao[u] = True
        canh_cay.append(best)
        xu = X[u]; yu = Y[u]
        for v in range(n):
            if not vao[v]:
                d = abs(xu - X[v]) + abs(yu - Y[v])
                if d < dist[v]:
                    dist[v] = d
    canh_cay = sorted(canh_cay[1:])            # bo "canh" 0 cua dinh goc
    with open('PHANCUM.OUT', 'w') as f:
        f.write(str(canh_cay[-(k - 1)]) + '\n')

main()
