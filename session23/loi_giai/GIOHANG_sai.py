# GIOHANG - BAN SAI (de chua bai): cap nhat TAI CHO nhu cai tui 0/1, duyet b giam dan, khong giu ban sao nhom.
# Duyet nguoc chi chan duoc viec lay MOT mon hai lan; mon thu hai cung nhom van doc f[b - w2] da chua mon thu
# nhat -> mua 2 mon cung nhom. Phan vi du: B = 10, nhom 1 co (4, 5) va (5, 6) -> in 11, dung la 6.
def main():
    data = open('GIOHANG.INP', 'rb').read().split()
    n, B = int(data[0]), int(data[1])
    nhom = {}
    pos = 2
    for _ in range(n):
        g, w, v = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        nhom.setdefault(g, []).append((w, v))
    f = [0] * (B + 1)
    for ds in nhom.values():
        for w, v in ds:
            for b in range(B, w - 1, -1):
                if f[b - w] + v > f[b]:
                    f[b] = f[b - w] + v      # SAI: f[b - w] co the da gom mon khac cung nhom
    with open('GIOHANG.OUT', 'w') as fo:
        fo.write(str(f[B]) + '\n')

main()
