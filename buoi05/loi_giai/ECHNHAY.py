# ECHNHAY: n hon da, hon i cao h[i]. Ech o hon 1, moi lan nhay tu hon i sang hon j voi
# i < j <= i + k, ton |h[i] - h[j]| suc. Suc it nhat de den hon n? n <= 10^5, k <= 20, h[i] <= 10^4
#   Trang thai : f[i] = suc it nhat de den hon i
#   Truy hoi   : f[i] = min( f[j] + |h[i] - h[j]| ) voi max(1, i-k) <= j < i  ("keo ve": nhin lai k hon truoc)
#   Khoi tao   : f[1] = 0
#   Thu tu     : i tang dan
#   Dap an     : f[n]
# O(n*k) = 2*10^6 phep -> ~0.2 s. Neu k den 100 thi 10^7 phep -> qua sat 1 giay voi Python.
# (Meo map(...) cua CATGO KHONG giup o day: cat lat f[j:i] moi buoc ton bang chinh vong lap ngan.)
def main():
    data = open('ECHNHAY.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    h = list(map(int, data[2:2 + n]))       # chi so tu 0: hon 1 la h[0]
    f = [0] * n
    for i in range(1, n):
        hi = h[i]
        tot = 1 << 60
        for j in range(max(0, i - k), i):
            v = f[j] + abs(hi - h[j])
            if v < tot:
                tot = v
        f[i] = tot
    with open('ECHNHAY.OUT', 'w') as out:
        out.write(str(f[n - 1]) + '\n')

main()
