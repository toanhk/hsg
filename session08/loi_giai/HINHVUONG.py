# HINHVUONG: bang m x n chi gom 0 va 1 (moi hang la mot xau). Tim canh hinh vuong lon nhat
# gom toan so 1. m, n <= 1000
#   Trang thai : f[i][j] = canh hinh vuong toan 1 lon nhat co goc DUOI-PHAI tai (i,j)
#   Truy hoi   : f[i][j] = 0 neu o (i,j) la 0,
#                nguoc lai 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])  (tren, trai, cheo tren-trai)
#   Khoi tao   : hang 0 va cot 0 gia (ngoai bang) = 0
#   Thu tu     : hang tren truoc, trai sang phai
#   Dap an     : max cua moi f[i][j]  (KHONG phai f[m][n])
# Giu hang tren `tren` (lech 1 o: tren[0] = 0 la cot gia); trai, cheo la 2 bien.
def main():
    data = open('HINHVUONG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    best = 0
    tren = [0] * (n + 1)
    for hang in data[2:2 + m]:                 # hang la bytes, hang[j] = 48 ('0') hoac 49 ('1')
        moi = [0]
        trai = cheo = 0
        for t, c in zip(tren[1:], hang):       # t = o tren; cheo = o tren-trai; trai = o ben trai
            if c == 49:
                v = t if t < trai else trai
                if cheo < v:
                    v = cheo
                v += 1
                if v > best:
                    best = v
            else:
                v = 0
            moi.append(v)
            trai = v
            cheo = t
        tren = moi
    with open('HINHVUONG.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
