# CUUHOA: ban do m x n: '.' duong, '#' nha cao tang (khong di qua), 'T' tram cuu hoa, 'H' nha dan.
# Xe cuu hoa moi phut di sang 1 o ke canh (tren/duoi/trai/phai), di qua duoc '.', 'T', 'H'.
# Voi moi nha dan, khoang cach = so phut it nhat tu tram GAN NHAT. In: so nha khong xe nao toi duoc,
# va tong khoang cach cua cac nha toi duoc.  m, n <= 1000 (10^6 o)
# BFS NHIEU NGUON: cho TAT CA tram vao lop 0 cung luc. Lop k = cac o cach tram gan nhat dung k buoc.
# (Tuong tuong them mot "sieu tram" noi toi moi tram bang canh 0 buoc.)  O(m*n)
# Toi uu cho Python (de kiem tra toc do):
#   - ma hoa o (i, j) thanh so i*W + j voi W = n + 2, them VIEN TUONG quanh bang -> khong kiem tra bien;
#   - mot bytearray 'da' gop ca "tuong" lan "da tham" -> moi o ke chi mot phep kiem tra;
#   - BFS theo TUNG LOP bang list (khong can deque, khong can mang khoang cach);
#   - dem nha trong moi lop bang sum(map(...)) chay trong C.
def main():
    data = open('CUUHOA.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    da = bytearray(b'\x01') * (W * (m + 2))            # 1 = tuong / da tham
    nha = bytearray(W * (m + 2))                         # 1 = nha dan
    bo_tuong = bytes.maketrans(b'.TH#', b'\x00\x00\x00\x01')
    bo_nha = bytes.maketrans(b'.TH#', b'\x00\x00\x01\x00')
    lop = []
    so_nha = 0
    for i in range(m):
        r = data[2 + i]
        base = (i + 1) * W + 1
        da[base:base + n] = r.translate(bo_tuong)
        nha[base:base + n] = r.translate(bo_nha)
        so_nha += r.count(b'H')
        j = r.find(b'T')
        while j >= 0:                                    # moi tram vao lop 0
            lop.append(base + j)
            da[base + j] = 1
            j = r.find(b'T', j + 1)
    toi = 0; tong = 0; k = 0
    nha_o = nha.__getitem__
    while lop:
        c = sum(map(nha_o, lop))                         # so nha o dung khoang cach k
        toi += c; tong += c * k
        moi = []
        for u in lop:
            for v in (u - W, u + W, u - 1, u + 1):
                if not da[v]:
                    da[v] = 1
                    moi.append(v)
        lop = moi; k += 1
    with open('CUUHOA.OUT', 'w') as f:
        f.write(f'{so_nha - toi} {tong}\n')

main()
