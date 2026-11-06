# LCS: do dai xau con chung dai nhat cua hai xau A, B (chu thuong, |A|, |B| <= 2000)
#   Trang thai : f[i][j] = LCS cua A[:i] va B[:j]  (i ky tu dau cua A, j ky tu dau cua B)
#   Truy hoi   : A[i-1] == B[j-1] -> f[i][j] = f[i-1][j-1] + 1
#                nguoc lai        -> f[i][j] = max(f[i-1][j], f[i][j-1])
#   Khoi tao   : f[0][j] = f[i][0] = 0 (mot xau rong)
#   Thu tu     : i tang, trong moi i thi j tang
#   Dap an     : f[n][m]
# Toi uu cho Python: hang i chi can hang i-1 -> giu 2 hang (truoc, hang);
# o ben trai f[i][j-1] giu trong bien c; duyet B bang enumerate thay cho B[j-1].
# 4*10^6 o ~ 0.4 s (LCS_bang.py dung bang 2 chieu dp[i][j] cham hon ~2 lan)
def main():
    data = open('LCS.INP', 'rb').read().split()
    A, B = data[0], data[1]                 # kieu bytes: duyet ra so nguyen (ma ky tu), so sanh nhanh
    m = len(B)
    truoc = [0] * (m + 1)
    for x in A:
        hang = [0]
        c = 0                               # c = hang[j], o ngay ben trai
        for j, y in enumerate(B):
            if x == y:
                c = truoc[j] + 1            # cheo: f[i-1][j-1]
            else:
                t = truoc[j + 1]            # tren: f[i-1][j]
                if t > c:
                    c = t
            hang.append(c)
        truoc = hang
    with open('LCS.OUT', 'w') as out:
        out.write(str(truoc[m]) + '\n')

main()
