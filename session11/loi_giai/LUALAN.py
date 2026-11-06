# LUALAN: khu rung m x n gom 'F' (o dang chay o phut 0), 'T' (cay), '.' (dat trong, lua khong qua).
# Moi phut, lua lan tu o dang chay sang moi o CAY ke canh. Hoi: (1) phut cuoi cung co o cay bat lua
# (0 neu khong o nao bat lua them), (2) so o cay khong bao gio chay. m, n <= 1000
# Mo hinh: thoi diem o cay chay = khoang cach ngan nhat tu O 'F' GAN NHAT -> BFS NHIEU NGUON:
# cho TAT CA o 'F' vao tang 0 cung luc, roi loang nhu BFS thuong.
# (Chay BFS rieng tu tung o F roi lay min: k nguon x 10^6 o -> qua cham. Xem LUALAN_tunguon.py)
# Vien '.' quanh bang; s la bytearray, doi o cay thanh 'F' khi no bat lua (vua la danh dau tham).
def main():
    data = open('LUALAN.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    vien = b'.' * W
    s = bytearray(vien + b''.join(b'.' + r + b'.' for r in data[2:2 + m]) + vien)
    CAY, LUA = 84, 70                        # 'T', 'F'
    tang = []                                # tang 0: moi o dang chay
    p = s.find(b'F')
    while p >= 0:
        tang.append(p)
        p = s.find(b'F', p + 1)
    phut = 0
    while True:
        ke = []
        for p in tang:
            for v in (p - W, p + W, p - 1, p + 1):
                if s[v] == CAY:
                    s[v] = LUA
                    ke.append(v)
        if not ke:
            break
        phut += 1
        tang = ke
    with open('LUALAN.OUT', 'w') as f:
        f.write(f'{phut} {s.count(CAY)}\n')

main()
