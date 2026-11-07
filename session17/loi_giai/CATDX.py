# CATDX: cat xau S thanh it doan nhat sao cho moi doan la xau doi xung (doc xuoi = doc nguoc). In so doan.
# |S| <= 2000, chu thuong.
# Hai lop QHD:
# (1) QHD tren doan - bang doi xung:
#   dx[l][r] = True neu S[l..r] doi xung;  dx[l][r] = (S[l] == S[r]) and (r - l < 2 or dx[l+1][r-1])
#   Thu tu: l giam dan (can hang l+1).
# (2) QHD mot chieu - so doan it nhat:
#   Trang thai : g[i] = so doan it nhat de cat tien to S[0..i-1]
#   Truy hoi   : doan CUOI la S[l..i-1] doi xung: g[i] = min(g[l] + 1) voi dx[l][i-1]
#   Khoi tao   : g[0] = 0;  Thu tu: i tang;  Dap an: g[n]
# Moi lop n^2/2 = 2*10^6 o voi n = 2000. Do: bang dx ~0,12 s; ca bai ~0,4 s.
# Meo: (2) can dx[l][i-1] voi i co dinh, l thay doi -> luu bang theo COT: cot[r] = danh sach l ma S[l..r] doi xung.
def main():
    data = open('CATDX.INP', 'rb').read().split()
    S = data[0]
    n = len(S)
    cot = [[] for _ in range(n)]               # cot[r] = cac l de S[l..r] doi xung
    sau = [False] * n                          # sau[r] = dx[l+1][r]
    for l in range(n - 1, -1, -1):
        x = S[l]
        hang = [False] * n
        hang[l] = True
        cot[l].append(l)
        for r in range(l + 1, n):
            if S[r] == x and (r - l < 2 or sau[r - 1]):
                hang[r] = True
                cot[r].append(l)
        sau = hang
    g = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = min([g[l] for l in cot[i - 1]]) + 1
    with open('CATDX.OUT', 'w') as out:
        out.write(str(g[n]) + '\n')

main()
