# DONGHANG: n kien hang xep hang theo thu tu, kien i nang a[i]. Chia day thanh cac doan LIEN TIEP, moi doan len
# mot xe: moi xe cho toi da K kien va tong khoi luong <= W. Cuoc mot xe = khoi luong kien NANG NHAT tren xe.
# Tong cuoc nho nhat? (Dam bao a[i] <= W.)  n <= 10^5, 1 <= K <= n, a[i] <= W <= 10^9; khi n > 2000 thi K <= 20.
# QHD mot chieu:
#   Trang thai : f[i] = tong cuoc nho nhat de cho xong i kien dau.
#   Cong thuc  : f[i] = min f[j] + max(a[j+1..i])  voi i-K <= j < i va sum(a[j+1..i]) <= W.
#   Khoi tao   : f[0] = 0.
#   Thu tu     : i tang dan; voi moi i, j giam dan tu i-1 de cap nhat max va tong "lui dan" trong O(1).
#   Dap an     : f[n].
# O(n*K) = 2*10^6 buoc (do: ~0,35 s).
def main():
    data = open('DONGHANG.INP', 'rb').read().split()
    n, K, W = int(data[0]), int(data[1]), int(data[2])
    a = [0] + list(map(int, data[3:3 + n]))
    INF = float('inf')
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        best = INF
        mx = 0; s = 0
        for j in range(i - 1, max(i - K, 0) - 1, -1):   # xe cuoi cho kien j+1..i
            x = a[j + 1]
            s += x
            if s > W:
                break
            if x > mx:
                mx = x
            v = f[j] + mx
            if v < best:
                best = v
        f[i] = best
    with open('DONGHANG.OUT', 'w') as fo:
        fo.write(str(f[n]) + '\n')

main()
