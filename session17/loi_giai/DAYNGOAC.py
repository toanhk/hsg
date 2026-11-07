# DAYNGOAC: xau S gom cac ky tu ( ) [ ]. Chen it ky tu nhat (vao vi tri bat ky) de duoc day ngoac DUNG
# (moi ngoac mo co ngoac dong cung loai, long nhau dung). In so ky tu phai chen.
# |S| <= 200.
# QHD tren doan:
#   Trang thai : f[l][r] = so ky tu it nhat can chen de S[l..r] thanh day dung (doan rong: 0)
#   Truy hoi   : xet ky tu dau S[l]:
#                - khong ghep voi ky tu nao trong doan: chen them ban sao cua no -> 1 + f[l+1][r]
#                - S[l] la ngoac MO va ghep voi S[k] (l < k <= r) la ngoac DONG cung loai:
#                  f[l+1][k-1] + f[k+1][r]   (ben trong cap va phan sau cap la hai bai doc lap)
#                f[l][r] = min cua cac truong hop tren
#   Khoi tao   : f[l][l] = 1, doan rong (l > r) = 0
#   Thu tu     : l giam dan, r tang dan
#   Dap an     : f[0][n-1]
# O(n^3/6) ~ 1,3*10^6 voi n = 200. Bang co them mot hang/cot 0 de "doan rong" khong can if.
def main():
    data = open('DAYNGOAC.INP', 'rb').read().split()
    S = data[0].decode()
    n = len(S)
    cap = {'(': ')', '[': ']'}
    f = [[0] * (n + 1) for _ in range(n + 2)]  # f[l][r+1] luu doan S[l..r]  (dich cot 1 de doan rong la f[l][l])
    for l in range(n - 1, -1, -1):
        fl = f[l]
        fs = f[l + 1]
        dong = cap.get(S[l])                   # None neu S[l] la ngoac dong
        for r in range(l, n):                  # tinh fl[r+1] = f(l..r)
            best = 1 + fs[r + 1]
            if dong:
                for k in range(l + 1, r + 1):
                    if S[k] == dong:
                        c = fs[k] + f[k + 1][r + 1]   # f(l+1..k-1) + f(k+1..r)
                        if c < best:
                            best = c
            fl[r + 1] = best
    with open('DAYNGOAC.OUT', 'w') as out:
        out.write(str(f[0][n]) + '\n')

main()
