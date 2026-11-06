# MUAVE: n nguoi xep hang mua ve, nguoi i mua mot minh mat t[i] giay; nguoi i mua giup ca nguoi
# i+1 mat r[i] giay; nguoi i mua giup ca i+1, i+2 mat s[i] giay. Tong thoi gian nho nhat de ca
# hang co ve. n <= 5*10^5, t, r, s <= 30000
#   Trang thai : f[i] = thoi gian nho nhat de i nguoi dau co ve
#   Truy hoi   : f[i] = min(f[i-1] + t[i], f[i-2] + r[i-1], f[i-3] + s[i-2])
#                (nhom cuoi cung gom 1, 2 hay 3 nguoi)
#   Khoi tao   : f[0] = 0; f[-1], f[-2] = vo cung (khong co nhom vuot dau hang)
#   Thu tu     : i tang dan
#   Dap an     : f[n]
# Chi can 3 gia tri cuoi -> 3 bien, chay mot vong zip.
def main():
    data = open('MUAVE.INP', 'rb').read().split()
    n = int(data[0])
    t = list(map(int, data[1:1 + n]))
    r = list(map(int, data[1 + n:n + n]))                    # n - 1 so
    s = list(map(int, data[n + n:n + n + n - 2]))            # n - 2 so
    INF = 10**18
    # a = f[i-3], b = f[i-2], c = f[i-1]; chi so i chay tu 1 (nguoi 1 = t[0])
    a, b, c = INF, INF, 0
    r = [INF] + r                                            # r[i-1] cho nhom (i-1, i): lech de i = 1 ra INF
    s = [INF, INF] + s
    for i in range(n):
        x = c + t[i]
        y = b + r[i]
        if y < x: x = y
        y = a + s[i]
        if y < x: x = y
        a, b, c = b, c, x
    with open('MUAVE.OUT', 'w') as f:
        f.write(str(c) + '\n')

main()
