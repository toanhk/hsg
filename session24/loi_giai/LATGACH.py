# LATGACH (de khoi dong buoi 24, bai 3) - QHD mot chieu dem co modulo (buoi 4-5)
# Dem so cach lat kin hanh lang 2 x n bang gach 1x2 (dat doc hoac ngang) va gach 2x2, modulo 10^9+7.
# T truy van n, T <= 10^5, 1 <= n <= 10^6.
# QHD:
#   Trang thai : f[i] = so cach lat 2 x i.
#   Cong thuc  : cot cuoi la 1 gach doc (f[i-1]), hoac 2 cot cuoi la 2 gach ngang hoac 1 gach 2x2 (2*f[i-2]).
#                f[i] = f[i-1] + 2 f[i-2].
#   Khoi tao   : f[0] = 1 (hanh lang rong co 1 cach: khong dat gi), f[1] = 1.
#   Thu tu     : i tang den max n (tinh MOT lan cho moi truy van).
#   Dap an     : f[n] cho tung truy van.
# Do ~0,15 s (10^6 buoc + mod).
def main():
    data = open('LATGACH.INP', 'rb').read().split()
    t = int(data[0])
    ns = list(map(int, data[1:1 + t]))
    M = max(ns)
    MOD = 10**9 + 7
    f = [0] * (M + 1)
    f[0] = 1
    if M >= 1:
        f[1] = 1
    for i in range(2, M + 1):
        f[i] = (f[i - 1] + 2 * f[i - 2]) % MOD
    with open('LATGACH.OUT', 'w') as fo:
        fo.write('\n'.join(str(f[n]) for n in ns) + '\n')

main()
