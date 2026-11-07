# GOPSOI: n dong soi xep thanh hang, dong thu i co a[i] vien. Moi buoc gop HAI DONG KE NHAU thanh mot dong,
# chi phi = tong so soi cua dong moi. Gop den khi con 1 dong; tim tong chi phi nho nhat.
# n <= 300, a[i] <= 10^9.
# QHD tren doan:
#   Trang thai : f[l][r] = chi phi nho nhat de gop cac dong l..r thanh MOT dong
#   Truy hoi   : lan gop CUOI CUNG noi hai khoi [l..k] va [k+1..r] (l <= k < r):
#                f[l][r] = min_k (f[l][k] + f[k+1][r]) + S(l, r),   S(l, r) = P[r+1] - P[l] (cong don)
#   Khoi tao   : f[i][i] = 0 (mot dong khong can gop)
#   Thu tu     : theo DO DAI doan d = r - l tang dan (doan ngan tinh truoc doan dai)
#   Dap an     : f[0][n-1]
# O(n^3/6) ~ 4,5*10^6 phep voi n = 300. Meo: min(map(add, ...)) chay vong trong bang C; can f[k+1][r]
# theo CHI SO k lien tiep -> luu them bang g[r][k] = f[k][r] (bang "theo cot") de cat lat duoc.
# Do (do_doan.py): n = 300 ~ 0,21 s (vong lap thuan 0,33 s).
from operator import add

def main():
    data = open('GOPSOI.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    P = [0] * (n + 1)                          # P[i] = a[0] + ... + a[i-1]
    for i in range(n):
        P[i + 1] = P[i] + a[i]
    f = [[0] * n for _ in range(n)]            # f[l][r]
    g = [[0] * n for _ in range(n)]            # g[r][l] = f[l][r]
    for d in range(1, n):                      # do dai doan - 1
        for l in range(n - d):
            r = l + d
            # k chay l..r-1: f[l][k] la f[l][l:r], f[k+1][r] la g[r][l+1:r+1]
            v = min(map(add, f[l][l:r], g[r][l + 1:r + 1])) + P[r + 1] - P[l]
            f[l][r] = v
            g[r][l] = v
    with open('GOPSOI.OUT', 'w') as out:
        out.write(str(f[0][n - 1]) + '\n')

main()
