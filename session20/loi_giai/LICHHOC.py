# LICHHOC: n mon hoc, m dieu kien "mon u phai hoc TRUOC mon v". Moi ky hoc dung 1 mon, hoc het n mon trong n ky.
# Dem so thu tu hoc hop le, lay du cho 10^9 + 7 (co vong dieu kien -> 0).   n <= 18, m <= n(n-1)/2.
# (Buoi 12 tim MOT thu tu bang Kahn; o day DEM tat ca - so thu tu co the toi n! nen khong liet ke duoc.)
#   Trang thai : f[mask] = so cach hoc DUNG cac mon trong mask o |mask| ky dau, hop le.
#   Cong thuc  : xet mon v hoc CUOI CUNG trong mask: hop le <=> moi mon tien quyet cua v deu nam trong mask bo v.
#                f[mask] = tong f[mask bo v]  voi v thuoc mask va truoc[v] la tap con cua (mask bo v).
#                (truoc[v] = mask cac mon phai hoc truoc v;  "A tap con B" <=> A & B == A.)
#   Khoi tao   : f[0] = 1 (chua hoc gi: 1 cach).
#   Thu tu     : mask tang dan.
#   Dap an     : f[2^n - 1].
# O(2^n * n): n = 18 -> 4,7*10^6, do ~0,27 s (do_bitmask.py). n = 20 mat ~1,1 s.
def main():
    data = open('LICHHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    MOD = 10**9 + 7
    truoc = [0] * n
    for k in range(m):
        u, v = int(data[2 + 2 * k]) - 1, int(data[3 + 2 * k]) - 1
        truoc[v] |= 1 << u
    N = 1 << n
    tq = {1 << j: truoc[j] for j in range(n)}  # 2^v -> tap tien quyet cua v
    f = [0] * N
    f[0] = 1
    for mask in range(1, N):
        s = 0
        mm = mask
        while mm:
            b = mm & -mm
            mm ^= b
            r = mask ^ b                      # hoc v = b cuoi cung, truoc do da hoc r
            t = tq[b]
            if r & t == t:
                s += f[r]
        f[mask] = s % MOD
    with open('LICHHOC.OUT', 'w') as fo:
        fo.write(str(f[N - 1]) + '\n')

main()
