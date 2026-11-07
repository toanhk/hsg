# NHANMT: nhan day n ma tran A1 * A2 * ... * An, Ai co kich thuoc p[i-1] x p[i].
# Nhan ma tran a x b voi b x c ton a*b*c phep nhan so. Dat ngoac de tong so phep nhan nho nhat.
# n <= 200, p[i] <= 1000.
# QHD tren doan (danh so ma tran 0..n-1, ma tran i co kich thuoc p[i] x p[i+1]):
#   Trang thai : f[l][r] = so phep nhan nho nhat de tinh tich A_l ... A_r
#   Truy hoi   : phep nhan CUOI CUNG la (A_l..A_k) * (A_k+1..A_r), hai khoi co kich thuoc
#                p[l] x p[k+1] va p[k+1] x p[r+1]:
#                f[l][r] = min_k f[l][k] + f[k+1][r] + p[l] * p[k+1] * p[r+1]
#   Khoi tao   : f[i][i] = 0
#   Thu tu     : l GIAM dan, r tang dan tu l+1 (f[k+1][r] co k+1 > l da tinh, f[l][k] co k < r da tinh)
#   Dap an     : f[0][n-1]
# O(n^3/6) ~ 1,3*10^6 voi n = 200 -> vong lap thuan du nhanh (~0,15 s).
def main():
    data = open('NHANMT.INP', 'rb').read().split()
    n = int(data[0])
    p = list(map(int, data[1:n + 2]))
    f = [[0] * n for _ in range(n)]
    for l in range(n - 2, -1, -1):
        fl = f[l]
        pl = p[l]
        for r in range(l + 1, n):
            t = pl * p[r + 1]                  # phan chung cua moi k
            best = -1
            for k in range(l, r):
                c = fl[k] + f[k + 1][r] + t * p[k + 1]
                if best < 0 or c < best:
                    best = c
            fl[r] = best
    with open('NHANMT.OUT', 'w') as out:
        out.write(str(f[0][n - 1]) + '\n')

main()
