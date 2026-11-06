# MANGDIEN - vet can (m <= 12): thu moi tap day (2^m). Voi mot tap day co dinh, cac lang chia thanh cac
# thanh phan lien thong; moi thanh phan can DUNG MOT tram, dat o lang re nhat cua thanh phan.
# Cach nay KHONG dung dinh ao -> dung de kiem cheo loi giai mau.
def main():
    data = open('MANGDIEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    c = [0] + list(map(int, data[2:2 + n]))
    p = 2 + n
    canh = [(int(data[p + 3 * i]), int(data[p + 3 * i + 1]), int(data[p + 3 * i + 2])) for i in range(m)]
    best = None
    for mask in range(1 << m):
        nhom = list(range(n + 1))              # gan nhan thanh phan ngay tho: doi het nhan
        tong = 0
        for i in range(m):
            if mask >> i & 1:
                u, v, w = canh[i]
                tong += w
                a, b = nhom[u], nhom[v]
                if a != b:
                    nhom = [a if x == b else x for x in nhom]
        re = {}
        for x in range(1, n + 1):
            g = nhom[x]
            if g not in re or c[x] < re[g]:
                re[g] = c[x]
        tong += sum(re.values())
        if best is None or tong < best:
            best = tong
    with open('MANGDIEN.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
