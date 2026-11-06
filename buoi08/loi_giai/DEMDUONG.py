# DEMDUONG: bang m x n, '.' la o trong, '#' la o cam. Dem so duong tu (1,1) den (m,n),
# moi buoc sang PHAI hoac XUONG, khong di vao o cam. In ket qua mod 10^9+7. m, n <= 1000
#   Trang thai : f[i][j] = so duong tu (1,1) den (i,j)
#   Truy hoi   : f[i][j] = 0 neu (i,j) cam, nguoc lai f[i-1][j] + f[i][j-1]
#   Khoi tao   : f[1][1] = 1 neu o (1,1) trong (dung yen la 1 cach); ngoai bang = 0
#   Thu tu     : hang tren truoc, trai sang phai
#   Dap an     : f[m][n]
# Giu 1 hang; thay % MOD bang tru co dieu kien (tong 2 so < 2*MOD nen tru 1 lan la du).
MOD = 10**9 + 7

def main():
    data = open('DEMDUONG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    luoi = data[2:2 + m]                      # moi hang la 1 chuoi bytes; luoi[i][j] la so: 46 '.', 35 '#'
    f = [0] * n
    f[0] = 1                                  # "o tren" cua (1,1) gia la 1 de f[1][1] = 1
    for hang in luoi:
        moi = []
        trai = 0
        for tren, c in zip(f, hang):
            if c == 35:                       # '#'
                trai = 0
            else:
                trai += tren
                if trai >= MOD:
                    trai -= MOD
            moi.append(trai)
        f = moi
    with open('DEMDUONG.OUT', 'w') as out:
        out.write(str(f[-1]) + '\n')

main()
