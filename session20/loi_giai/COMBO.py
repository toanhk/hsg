# COMBO: can mua du n mon do (danh so 1..n). Cua hang ban m goi, goi j gia g[j] gom mot so mon.
# Mua mot so goi sao cho moi mon co trong it nhat mot goi da mua (thua cung duoc). Chi phi nho nhat? Khong du -> -1.
# n <= 15, m <= 100, g[j] <= 10^6.
# Moi goi = mot tap mon = mot so nguyen s[j] (bit t bat <=> goi co mon t+1).
#   Trang thai : dp[mask] = chi phi nho nhat de co (it nhat) cac mon trong mask... chinh xac hon: co DUNG tap mask
#                tu cac goi da mua (hop cac goi = mask).
#   Cong thuc  : (day toi) tu dp[mask] mua them goi j -> dp[mask | s[j]] = min(..., dp[mask] + g[j]).
#   Khoi tao   : dp[0] = 0, con lai vo cuc.
#   Thu tu     : mask tang dan (mask | s[j] >= mask; bang nhau thi chi ton tien, khong lam tot hon).
#   Dap an     : dp[2^n - 1] (vo cuc -> -1).
# O(2^n * m) = 3,3*10^6 phep thu, do ~0,3 s (test xau nhat). Gop goi trung tap (giu goi re nhat) de bot m.
def main():
    data = open('COMBO.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    pos = 2
    re = {}                                   # tap mon -> gia re nhat
    for _ in range(m):
        g, k = int(data[pos]), int(data[pos + 1]); pos += 2
        s = 0
        for t in data[pos:pos + k]:
            s |= 1 << (int(t) - 1)
        pos += k
        if s and (s not in re or g < re[s]):
            re[s] = g
    goi = list(re.items())
    INF = 10**18
    N = 1 << n
    dp = [INF] * N
    dp[0] = 0
    for mask in range(N - 1):                 # mask = N-1 da du, khong can mua them
        x = dp[mask]
        if x == INF:
            continue
        for s, g in goi:
            nm = mask | s
            if x + g < dp[nm]:
                dp[nm] = x + g
    with open('COMBO.OUT', 'w') as f:
        f.write(str(dp[N - 1] if dp[N - 1] < INF else -1) + '\n')

main()
