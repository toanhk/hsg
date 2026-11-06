# HONUOC: ban do m x n, '#' la dat, '.' la nuoc. Nuoc thong ra BIEN neu tu no di qua cac o nuoc
# ke canh toi duoc mot o nuoc nam o hang/cot ngoai cung. Moi vung nuoc lien thong KHONG thong
# ra bien la mot HO. In so ho va tong dien tich cac ho. m, n <= 1000
# Y tuong "loang tu bien": xoa het nuoc bien truoc, phan nuoc con lai chinh la cac ho -> dem thanh phan.
# Meo: lot quanh bang 1 vong NUOC (vong trong) roi 1 vong DAT (vong ngoai), W = n + 4.
#   Vong nuoc noi moi o nuoc o mep bang voi nhau -> CHI CAN LOANG 1 LAN tu o (1,1) cua vong nuoc la
#   xoa duoc toan bo bien. Vong dat ngoai cung de khong bao gio ra ngoai mang.
def loang(s, goc, W):                        # doi ca vung nuoc chua goc thanh dat, tra ve so o
    s[goc] = 35
    st = [goc]
    dem = 0
    while st:
        p = st.pop()
        dem += 1
        for v in (p - W, p + W, p - 1, p + 1):
            if s[v] == 46:
                s[v] = 35
                st.append(v)
    return dem

def main():
    data = open('HONUOC.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 4
    ngoai = b'#' * W
    trong = b'#' + b'.' * (n + 2) + b'#'
    s = bytearray(ngoai + trong + b''.join(b'#.' + r + b'.#' for r in data[2:2 + m]) + trong + ngoai)
    loang(s, W + 1, W)                       # xoa nuoc bien
    so_ho = 0
    tong = 0
    goc = s.find(b'.')
    while goc >= 0:
        so_ho += 1
        tong += loang(s, goc, W)
        goc = s.find(b'.', goc)
    with open('HONUOC.OUT', 'w') as f:
        f.write(f'{so_ho} {tong}\n')

main()
