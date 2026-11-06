# VANG: robot di tu (1,1) den (m,n), moi buoc XUONG (D) hoac PHAI (R). O so >= 0 la so vang
# robot nhat duoc khi di qua, o -1 la da (khong di vao). In tong vang lon nhat va duong di;
# neu nhieu duong cung tong lon nhat, in duong co thu tu tu dien NHO NHAT ('D' < 'R').
# Khong co duong thi in -1. m, n <= 1000
#   Trang thai : g[i][j] = vang lon nhat nhat duoc tren duong tu (i,j) DEN DICH (m,n)
#   Truy hoi   : g[i][j] = a[i][j] + max(g[i+1][j], g[i][j+1]); o da hoac khong toi dich -> AM
#   Khoi tao   : g[m][n] = a[m][n] (neu khong phai da)
#   Thu tu     : hang duoi truoc, trong hang phai sang trai (nguoc chieu di)
#   Dap an     : g[1][1]; truy vet XUOI tu (1,1): di D neu o duoi van giu duoc toi uu, khong thi R
# Vi sao tinh tu dich ve? Khi dung o (i,j) ta can biet "di xuong co con toi uu khong" -> can
# gia tri tu o ke DEN DICH. Chon D som nhat co the chinh la tu dien nho nhat.
# (Truy vet nguoc tu dich voi bang xuoi khong cho duoc tu dien nho nhat: xem VANG_nguoc.py.)
def main():
    data = open('VANG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + m * n]))
    AM = -1                                    # vang >= 0 nen dung -1 lam "khong toi dich duoc"
    g = [None] * m
    duoi = [AM] * (n + 1)                      # hang m+1 gia, them cot n+1 gia
    for i in range(m - 1, -1, -1):
        hang = a[i * n:(i + 1) * n]
        moi = [AM] * (n + 1)
        phai = AM
        for j in range(n - 1, -1, -1):
            v = hang[j]
            if v < 0:
                phai = AM
            else:
                d = duoi[j]
                b = d if d > phai else phai
                if b >= 0:
                    phai = b + v
                elif i == m - 1 and j == n - 1:
                    phai = v                   # chinh o dich
                else:
                    phai = AM
            moi[j] = phai
        g[i] = moi
        duoi = moi
    out = []
    if g[0][0] < 0:
        out.append('-1')
    else:
        out.append(str(g[0][0]))
        buoc = []
        i = j = 0
        while i < m - 1 or j < n - 1:
            can = g[i][j] - a[i * n + j]       # gia tri phan con lai phai dat
            if i + 1 < m and g[i + 1][j] == can:
                buoc.append('D'); i += 1
            else:
                buoc.append('R'); j += 1
        out.append(''.join(buoc))
    with open('VANG.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
