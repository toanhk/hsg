# TUIVOHAN: cai tui KHONG gioi han. n loai do vat, loai i nang w[i], gia tri v[i],
# moi loai lay bao nhieu cai cung duoc. Tui chiu W. n <= 100, W <= 5*10^4
#   Trang thai : f[s] = gia tri lon nhat voi tong khoi luong <= s, chi dung cac loai DA XET
#   Truy hoi   : f[s] = max(f[s], f[s - w] + v)
#   Khoi tao   : f[s] = 0
#   Thu tu     : vong ngoai la loai, vong trong s TANG dan (f[s - w] co the da chua loai nay -> lay lai duoc)
#   Dap an     : f[W]
# Chi khac TUI01 dung MOT cho: chieu duyet s. Giong DOITIEN buoi 4 (dem -> max).
# O(n * W) = 5*10^6 o ~ 0.21 s
def main():
    data = open('TUIVOHAN.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    f = [0] * (W + 1)
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        for s in range(w, W + 1):              # s tang dan
            x = f[s - w] + v
            if x > f[s]:
                f[s] = x
    with open('TUIVOHAN.OUT', 'w') as out:
        out.write(str(f[W]) + '\n')

main()
