# XEPLICH - THAM LAM SAI (de doi chieu): "chon viec ket thuc som nhat, bo cac viec trung no".
# Dung khi moi viec cung tien (bai xep lich kinh dien), SAI khi tien khac nhau:
#   viec [1, 2] gia 1 va [1, 10] gia 100: tham lam chon viec dau (1), toi uu la 100.
def main():
    data = open('XEPLICH.INP', 'rb').read().split()
    n = int(data[0])
    viec = sorted((int(data[2 + 3 * i]), int(data[1 + 3 * i]), int(data[3 + 3 * i])) for i in range(n))
    cuoi = 0; tong = 0
    for e, s, p in viec:
        if s > cuoi:
            tong += p; cuoi = e
    with open('XEPLICH.OUT', 'w') as fo:
        fo.write(str(tong) + '\n')

main()
