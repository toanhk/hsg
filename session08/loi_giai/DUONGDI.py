# DUONGDI: bang m x n so nguyen, di tu o (1,1) den o (m,n), moi buoc sang PHAI hoac XUONG.
# Tong lon nhat cac o di qua? m, n <= 1000, |a[i][j]| <= 10^9
#   Trang thai : f[i][j] = tong lon nhat cua mot duong tu (1,1) den (i,j)
#   Truy hoi   : f[i][j] = a[i][j] + max(f[i-1][j], f[i][j-1])   (buoc cuoi den tu TREN hoac TRAI)
#   Khoi tao   : f[1][1] = a[1][1]; o ngoai bang coi nhu -vo cung (khong den tu do duoc)
#   Thu tu     : hang tren truoc, trong hang trai sang phai
#   Dap an     : f[m][n]
# f[i] chi can hang f[i-1] -> giu 1 hang f: truoc khi ghi de, f[j] dang la "o tren";
# bien trai la o ben trai vua tinh. 10^6 o ~0.05 s (xem do_luoi.py).
from itertools import accumulate

def main():
    data = open('DUONGDI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + m * n]))
    f = list(accumulate(a[0:n]))              # hang 1: chi den duoc tu ben trai -> cong don
    for i in range(1, m):
        hang = a[i * n:(i + 1) * n]
        moi = []
        trai = -10**18                        # o (i, 0) khong co ben trai
        for tren, v in zip(f, hang):
            trai = (tren if tren > trai else trai) + v
            moi.append(trai)
        f = moi
    with open('DUONGDI.OUT', 'w') as out:
        out.write(str(f[-1]) + '\n')

main()
