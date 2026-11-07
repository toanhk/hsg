# PHANCONG: n nguoi, n viec; nguoi i lam viec j mat c[i][j] phut. Moi nguoi nhan DUNG mot viec, moi viec
# dung mot nguoi. Tong thoi gian nho nhat?   n <= 18, c[i][j] <= 10^6.
# Vet can n! hoan vi chi chay toi n ~ 9. QHD bitmask:
#   Trang thai : dp[mask] = tong nho nhat khi giao xong cac viec trong mask cho k = (so bit 1 cua mask)
#                nguoi DAU TIEN (nguoi 0..k-1). Nguoi nao lam thi da biet: chinh la so bit, khong can luu.
#   Cong thuc  : dp[mask] = min dp[mask bo j] + c[k-1][j]   voi moi viec j thuoc mask (nguoi k-1 lam j).
#   Khoi tao   : dp[0] = 0.
#   Thu tu     : mask tang dan (mask bo j luon NHO hon mask).
#   Dap an     : dp[2^n - 1].
# O(2^n * n): n = 18 -> 4,7*10^6 buoc, do ~0,25 s (do_bitmask.py). n = 20 da mat ~1,1 s -> QUA GIO voi Python.
def main():
    data = open('PHANCONG.INP', 'rb').read().split()
    n = int(data[0])
    c = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    N = 1 << n
    pc = [0] * N                              # pc[mask] = so bit 1 cua mask (tinh truoc, khong goi bin())
    for m in range(1, N):
        pc[m] = pc[m >> 1] + (m & 1)
    vt = {1 << j: j for j in range(n)}        # 2^j -> j
    dp = [0] * N
    for mask in range(1, N):
        row = c[pc[mask] - 1]                 # nguoi vua duoc giao viec
        best = 10**18
        m = mask
        while m:                              # duyet cac bit 1 cua mask
            b = m & -m                        # bit 1 thap nhat
            v = dp[mask ^ b] + row[vt[b]]
            if v < best:
                best = v
            m ^= b                            # xoa bit vua xet
        dp[mask] = best
    with open('PHANCONG.OUT', 'w') as f:
        f.write(str(dp[N - 1]) + '\n')

main()
