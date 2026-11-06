# CHIAKEO: n goi keo, goi i co a[i] vien. Chia moi goi cho mot trong hai ban (khong boc goi)
# sao cho chenh lech so keo hai ban nhan la nho nhat. n <= 500, a[i] <= 2000 (tong <= 10^6)
# Mo hinh: chon tap con co tong t <= tong/2 lon nhat -> dap an = tong - 2t (cai tui 0/1 "co/khong").
#   Trang thai : duoc[s] = 1 neu tao duoc tong s tu cac goi da xet
#   Truy hoi   : xet goi a: duoc[s] |= duoc[s - a]   (s giam dan, giong TUI01)
#   Khoi tao   : duoc[0] = 1
#   Dap an     : s lon nhat <= tong/2 co duoc[s] = 1
# Vong lap thuong: n * tong/2 = 2.5*10^8 phep -> qua gio (CHIAKEO_mang.py chi qua subtask 2).
# Meo Python: coi ca mang duoc[] la MOT so nguyen lon, bit s = duoc[s].
#   "duoc[s] |= duoc[s - a] voi moi s"  <=>  bits |= bits << a   (mot phep, chay trong C)
# Phep dich tren so 5*10^5 bit ~ vai micro giay -> ca bai ~ 0.03 s.
def main():
    data = open('CHIAKEO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tong = sum(a)
    nua = tong // 2
    mat_na = (1 << (nua + 1)) - 1              # chi giu cac bit 0..nua cho so khong phinh to
    bits = 1                                   # chi tao duoc tong 0
    for x in a:
        bits = (bits | (bits << x)) & mat_na
    t = bits.bit_length() - 1                  # bit cao nhat = tong lon nhat <= nua tao duoc
    with open('CHIAKEO.OUT', 'w') as out:
        out.write(str(tong - 2 * t) + '\n')

main()
