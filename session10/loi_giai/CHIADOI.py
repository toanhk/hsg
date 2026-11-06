# CHIADOI: n hoc sinh, m cap "khong hop nhau". Chia ca lop thanh hai doi (moi nguoi dung mot doi,
# doi co the rong) sao cho khong cap nao khong hop nhau o cung doi. Neu khong chia duoc in -1;
# nguoc lai in chenh lech |doi 1 - doi 2| NHO NHAT. n <= 10^5, m <= 2*10^5.
# Buoc 1 (DFS hai phia, nhu HAIPHIA): moi thanh phan lien thong to duoc 2 mau voi so dinh a_i, b_i,
#   neu khong to duoc -> -1. Trong mot thanh phan, phia a_i phai cung doi, phia b_i o doi kia;
#   chi duoc chon "lat" hay khong. Dinh co lap: a = 1, b = 0.
# Buoc 2 (cai tui, buoi 6): chenh lech = tong (+-d_i) voi d_i = |a_i - b_i|, D = tong d_i.
#   Chon tap S cac thanh phan bi lat dau tru: chenh lech = D - 2*tong(S). Can tap con co tong s
#   gan D/2 nhat -> bai tap tong (subset sum) voi tong <= D <= n.
#   QHD: f[s] = True neu tao duoc tong s.  f[0] = True; them vat d: f[s] |= f[s - d].
#   Dung so nguyen lon lam mang bit (buoi 6): bits |= bits << d (bit s bat <=> f[s] = True).
# Toc do: co the co toi 10^5 thanh phan (vi du 10^5 dinh co lap, d = 1) -> 10^5 phep dich so 10^5 bit
#   van cham. Nhung tong cac d_i <= n nen so GIA TRI KHAC NHAU cua d_i chi ~ sqrt(2n) ~ 450.
#   Gom cac d bang nhau: k vat gia tri d tach nhi phan thanh goi 1, 2, 4, ..., phan du
#   (moi so luong 0..k deu ghep duoc) -> chi con vai nghin phep dich. ~0.3 s ca doc input.

def main():
    data = open('CHIADOI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)

    # Buoc 1: DFS to hai mau tung thanh phan, dem so luong d = |a - b|
    mau = [-1] * (n + 1)
    so_luong = {}                              # so_luong[d] = so thanh phan co chenh lech d
    for s in range(1, n + 1):
        if mau[s] != -1:
            continue
        mau[s] = 0
        st = [s]
        dem = [1, 0]                           # dem[0], dem[1] = so dinh mau 0, mau 1
        while st:
            u = st.pop()
            khac = 1 - mau[u]
            for v in ke[u]:
                if mau[v] == -1:
                    mau[v] = khac
                    dem[khac] += 1
                    st.append(v)
                elif mau[v] != khac:
                    with open('CHIADOI.OUT', 'w') as out:
                        out.write('-1\n')
                    return
        d = abs(dem[0] - dem[1])
        if d:
            so_luong[d] = so_luong.get(d, 0) + 1

    # Buoc 2: tap tong bang mang bit, gom vat cung gia tri + tach nhi phan
    D = 0
    bits = 1                                   # chi tong 0 tao duoc
    for d, k in so_luong.items():
        D += d * k
        goi = 1
        while k > 0:
            lay = goi if goi < k else k        # goi 1, 2, 4, ... va phan con lai
            bits |= bits << (d * lay)
            k -= lay
            goi *= 2

    # tong s <= D/2 lon nhat tao duoc: cat bits giu cac bit 0..D//2, lay bit cao nhat
    s = (bits & ((1 << (D // 2 + 1)) - 1)).bit_length() - 1
    with open('CHIADOI.OUT', 'w') as out:
        out.write(str(D - 2 * s) + '\n')

main()
