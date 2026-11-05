# DIENDAU: giua hai chu so ke nhau dien '+', '-' hoac khong dien gi (noi lien thanh so nhieu chu so).
# Dem so cach de bieu thuc co gia tri S. n <= 12 chu so -> 3^11 = 177147 cach
# Khong dung eval: mang theo trang thai (tong cac so hang da xong, so hang dang viet do, dau cua no)
def main():
    data = open('DIENDAU.INP', 'rb').read().split()
    d = [int(ch) for ch in data[0].decode()]
    S = int(data[1])
    n = len(d)
    dem = 0

    def thu(i, tong, so, dau):           # da xu ly d[0..i-1]; 'so' la so hang dang viet do (chua cong)
        nonlocal dem
        if i == n:
            if tong + dau * so == S:
                dem += 1
            return
        x = d[i]
        thu(i + 1, tong, so * 10 + x, dau)          # khong dien: noi x vao so hang hien tai
        t = tong + dau * so                          # dong so hang hien tai lai
        thu(i + 1, t, x, 1)                          # dien '+'
        thu(i + 1, t, x, -1)                         # dien '-'

    thu(1, 0, d[0], 1)                   # chu so dau tien luon mang dau +
    with open('DIENDAU.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
