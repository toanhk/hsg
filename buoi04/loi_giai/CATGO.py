# CATGO: thanh go dai n, doan dai i ban duoc p[i]. Cat thanh cac doan nguyen (co the khong cat).
# Tong tien lon nhat? n <= 4000
#   Trang thai : f[i] = so tien lon nhat khi ban mot thanh dai i
#   Truy hoi   : f[i] = max( p[j] + f[i - j] ) voi j = 1..i  (j = do dai doan cat ra DAU TIEN)
#   Khoi tao   : f[0] = 0
#   Thu tu     : i tang dan
#   Dap an     : f[n]
# O(n^2 / 2) = 8*10^6 phep -> vong lap Python thuong (CATGO_vonglap.py) mat ~0.5 s tren may manh,
# may phong thi cham hon co the vuot 1 s. Toi uu: vong trong giao cho ham viet bang C:
# map(add, p[1..i], f[i-1..0]) tinh het cac tong p[j] + f[i-j], max(...) lay lon nhat -> ~0.3 s.
from operator import add

def main():
    data = open('CATGO.INP', 'rb').read().split()
    n = int(data[0])
    p = [0] + list(map(int, data[1:1 + n]))       # p[1..n]
    f = [0]                                        # f[0] = 0
    for i in range(1, n + 1):
        # reversed(f) khi f dang co i phan tu = f[i-1], f[i-2], ..., f[0]; ghep cap voi p[1], p[2], ..., p[i]
        f.append(max(map(add, p[1:i + 1], reversed(f))))
    with open('CATGO.OUT', 'w') as out:
        out.write(str(f[n]) + '\n')

main()
