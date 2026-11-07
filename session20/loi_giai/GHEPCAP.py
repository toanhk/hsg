# GHEPCAP: lop co n hoc sinh (n chan). Hai ban i, j ngoi cung ban thi "do an y" la a[i][j] (= a[j][i]).
# Xep n hoc sinh thanh n/2 cap sao cho tong do an y cua cac cap LON nhat.   n <= 20, a[i][j] <= 10^6.
# QHD bitmask + MEO BIT THAP NHAT:
#   Trang thai : dp[mask] = tong lon nhat khi cac ban trong mask da duoc xep cap (mask co so bit chan).
#   Chuyen     : (day toi) i = ban CHUA xep co so hieu NHO nhat; ban i kieu gi cung phai ngoi voi ai do,
#                nen chi thu ghep i voi tung ban j chua xep: dp[mask | i | j] = max(..., dp[mask] + a[i][j]).
#                (Neu thu MOI cap i < j thi moi cach xep bi dem lai (n/2)! lan va cham gap ~n lan.)
#   Khoi tao   : dp[0] = 0, con lai -1 (chua toi duoc).
#   Thu tu     : mask tang dan; bo qua mask chua toi duoc.
#   Dap an     : dp[2^n - 1].
# Nho meo bit thap nhat, chi ~1,1*10^4 mask (voi n = 20) thuc su toi duoc -> vong 2^20 mask phan lon la "continue".
# Do ~0,05 s voi n = 20; ban keo ve tren MOI mask (GHEPCAP_cham.py) mat ~1 s.
def main():
    data = open('GHEPCAP.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    N = 1 << n
    vt = {1 << j: j for j in range(n)}
    dp = [-1] * N
    dp[0] = 0
    for mask in range(N - 1):
        x = dp[mask]
        if x < 0:
            continue
        tu_do = (N - 1) ^ mask                # cac ban chua xep
        b = tu_do & -tu_do                    # ban chua xep so hieu nho nhat
        row = a[vt[b]]
        mb = mask | b
        m = tu_do ^ b
        while m:                              # thu ghep b voi tung ban c con lai
            c = m & -m
            m ^= c
            y = x + row[vt[c]]
            if y > dp[mb | c]:
                dp[mb | c] = y
    with open('GHEPCAP.OUT', 'w') as f:
        f.write(str(dp[N - 1]) + '\n')

main()
