# DEMXAU: dem xau nhi phan do dai n KHONG chua k so 1 lien tiep, mod 10^9+7. n <= 10^6, 1 <= k <= n
# Meo: them mot so 0 "ao" vao cuoi -> xau hop le do dai n <-> xau hop le do dai n+1 ket thuc bang 0.
# Xau ket thuc bang 0 = (xau ket thuc bang 0, hoac rong) + t so 1 (0 <= t <= k-1) + mot so 0.
#   Trang thai : h[i] = so xau hop le do dai i ket thuc bang 0 (h[0] = 1: xau rong)
#   Truy hoi   : h[i] = h[i-1] + h[i-2] + ... + h[i-k]   (bo qua chi so am)
#   Khoi tao   : h[0] = 1
#   Thu tu     : i tang dan; giu tong k so cuoi trong bien 'cua_so' (cong o moi, tru o roi khoi cua so)
#   Dap an     : h[n + 1]
# Neu cong lai k so moi buoc thi O(n*k) = 10^12 khi k lon -> phai dung cua so truot, O(n).
# k = 2: h la day Fibonacci (dung bai XAUNP buoi 3).
MOD = 10**9 + 7

def main():
    data = open('DEMXAU.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    h = [0] * (n + 2)
    h[0] = 1
    cua_so = 1                          # = h[i-1] + ... + h[i-k] khi bat dau buoc i
    for i in range(1, n + 2):
        h[i] = cua_so
        cua_so += h[i]                  # h[i] vao cua so
        if i - k >= 0:
            cua_so -= h[i - k]          # h[i-k] ra khoi cua so
        cua_so %= MOD                   # Python % luon tra so khong am, ke ca khi cua_so < 0
    with open('DEMXAU.OUT', 'w') as out:
        out.write(str(h[n + 1]) + '\n')

main()
