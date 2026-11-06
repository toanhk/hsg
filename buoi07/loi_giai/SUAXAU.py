# SUAXAU: so phep it nhat (chen, xoa, thay 1 ky tu) bien xau A thanh xau B. |A|, |B| <= 1500
#   Trang thai : f[i][j] = so phep it nhat bien A[:i] thanh B[:j]
#   Truy hoi   : A[i-1] == B[j-1] -> f[i][j] = f[i-1][j-1]          (giu nguyen ky tu cuoi)
#                nguoc lai -> 1 + min( f[i-1][j-1]   thay A[i-1] bang B[j-1]
#                                      f[i-1][j]     xoa A[i-1]
#                                      f[i][j-1] )   chen B[j-1] vao cuoi
#   Khoi tao   : f[i][0] = i (xoa het), f[0][j] = j (chen het)
#   Thu tu     : i tang, j tang
#   Dap an     : f[n][m]
# Giu 2 hang nhu LCS.py; KHAC LCS o khoi tao: o dau moi hang la i chu khong phai 0.
# 2.25*10^6 o ~ 0.3 s
def main():
    data = open('SUAXAU.INP', 'rb').read().split()
    A, B = data[0], data[1]
    m = len(B)
    truoc = list(range(m + 1))              # hang 0: f[0][j] = j
    for i, x in enumerate(A, 1):
        hang = [i]
        c = i                               # c = f[i][j] vua tinh (o ben trai)
        for j, y in enumerate(B):
            if x == y:
                c = truoc[j]
            else:
                t = truoc[j]                # cheo
                u = truoc[j + 1]            # tren
                if u < t:
                    t = u
                if c < t:
                    t = c
                c = t + 1
            hang.append(c)
        truoc = hang
    with open('SUAXAU.OUT', 'w') as out:
        out.write(str(truoc[m]) + '\n')

main()
