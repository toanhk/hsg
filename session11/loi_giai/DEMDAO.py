# DEMDAO: ban do m x n, '#' la dat, '.' la nuoc. Hai o dat chung CANH thuoc cung mot dao.
# In so dao va dien tich (so o) cua dao lon nhat. m, n <= 1000
# Mo hinh: dinh = o dat, canh = hai o dat ke canh -> dem thanh phan lien thong.
# Cach lam: duyet moi o; gap o dat chua tham -> them 1 dao, LOANG (DFS bang ngan xep) danh dau ca dao.
# Meo toc do (xem do_loang.py):
#  - Them VIEN nuoc quanh bang, W = n + 2, o (i,j) -> p = (i+1)*W + (j+1). 4 o ke la p-W, p+W, p-1, p+1,
#    khong bao gio ra ngoai mang -> khong can kiem tra bien.
#  - Danh dau "da tham" bang cach doi o dat thanh nuoc ngay khi DAY vao ngan xep (khong bi day 2 lan).
#  - Tim o dat tiep theo bang s.find(b'#', vi tri) (chay trong C).
# Do phuc tap O(m*n): moi o day/lay khoi ngan xep toi da 1 lan. 10^6 o ~0.2 s.
def main():
    data = open('DEMDAO.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    vien = b'.' * W
    s = bytearray(vien + b''.join(b'.' + r + b'.' for r in data[2:2 + m]) + vien)
    DAT, NUOC = 35, 46                       # ma ASCII cua '#' va '.'
    so_dao = 0
    lon_nhat = 0
    goc = s.find(b'#')
    while goc >= 0:
        so_dao += 1
        s[goc] = NUOC
        st = [goc]
        dien_tich = 0
        while st:
            p = st.pop()
            dien_tich += 1
            for v in (p - W, p + W, p - 1, p + 1):
                if s[v] == DAT:
                    s[v] = NUOC              # danh dau ngay khi day vao
                    st.append(v)
        if dien_tich > lon_nhat:
            lon_nhat = dien_tich
        goc = s.find(b'#', goc)              # o truoc goc deu da la nuoc
    with open('DEMDAO.OUT', 'w') as f:
        f.write(f'{so_dao} {lon_nhat}\n')

main()
