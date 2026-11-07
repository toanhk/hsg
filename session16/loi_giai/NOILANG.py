# NOILANG: n lang, m con duong CO THE xay (u, v, chi phi w). Chon mot so duong de xay sao cho giua hai lang
# bat ky deu di duoc (truc tiep hoac qua lang khac), tong chi phi nho nhat. Khong the thi in -1.
# n <= 10^5, m <= 2*10^5, w <= 10^9.
# Kruskal: xet canh theo chi phi TANG DAN; canh noi hai thanh phan KHAC nhau thi chon (hop hai thanh phan),
# canh noi hai lang da lien thong thi bo (se tao chu trinh). Du n-1 canh -> xong.
# DSU: parent[] + size[], find viet bang VONG LAP (nen nua duong), hop theo kich thuoc.
# O(m log m) cho sap xep + gan O(m) cho DSU. Do: ~0,27 s voi m = 2*10^5 (do_khung.py).
def main():
    data = open('NOILANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    U = list(map(int, data[2:2 + 3 * m:3]))
    V = list(map(int, data[3:3 + 3 * m:3]))
    W = list(map(int, data[4:4 + 3 * m:3]))
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    tong = 0
    chon = 0                                   # so canh da chon
    for i in sorted(range(m), key=W.__getitem__):   # chi so canh theo w tang dan
        if chon == n - 1:
            break
        a = U[i]
        while parent[a] != a:                  # find(a) khong de quy
            parent[a] = parent[parent[a]]      # nen nua duong: tro len ong
            a = parent[a]
        b = V[i]
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a == b:
            continue                           # da lien thong -> canh thua
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a                          # gan cay nho vao cay lon
        size[a] += size[b]
        tong += W[i]
        chon += 1
    with open('NOILANG.OUT', 'w') as f:
        f.write(str(tong if chon == n - 1 else -1) + '\n')

main()
