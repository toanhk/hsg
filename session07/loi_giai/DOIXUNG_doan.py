# DOIXUNG - QHD tren doan (bao truoc buoi 17):
#   Trang thai : f[l][r] = do dai xau doi xung dai nhat xoa duoc tu S[l..r]
#   Truy hoi   : S[l] == S[r] -> f[l][r] = f[l+1][r-1] + 2
#                nguoc lai    -> f[l][r] = max(f[l+1][r], f[l][r-1])
#   Khoi tao   : f[l][l] = 1, doan rong = 0
#   Thu tu     : l GIAM dan (can hang l+1), r tang dan tu l
#   Dap an     : f[0][n-1]
# So o = n^2/2 = 2*10^6, it hon LCS(S, dao S) mot nua; giu 2 hang theo l.
def main():
    data = open('DOIXUNG.INP', 'rb').read().split()
    S = data[0]
    n = len(S)
    sau = [0] * (n + 1)                     # hang l+1: sau[r] = f[l+1][r]
    for l in range(n - 1, -1, -1):
        x = S[l]
        hang = [0] * (n + 1)
        hang[l] = 1
        c = 1                               # c = f[l][r-1]
        for r in range(l + 1, n):
            if S[r] == x:
                c = (sau[r - 1] if r - 1 >= l + 1 else 0) + 2
            else:
                t = sau[r]
                if t > c:
                    c = t
            hang[r] = c
        sau = hang
    with open('DOIXUNG.OUT', 'w') as out:
        out.write(str(sau[n - 1]) + '\n')

main()
