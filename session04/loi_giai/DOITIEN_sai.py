# DOITIEN - BAN SAI de chua tren lop: dao thu tu 2 vong lap (s o ngoai, loai tien o trong).
# Ban nay dem DAY to tien co thu tu: voi S = 3, to {1, 2} no dem 1+2 va 2+1 la 2 cach (dung la 1).
# Thuc chat day la bai CAUTHANG voi buoc nhay = cac menh gia. Chay cham_thu de thay chi dung 2/10 test - test nao moi cach doi chi dung 1 loai to thi hai cach dem moi trung nhau.
MOD = 10**9 + 7

def main():
    data = open('DOITIEN.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + m]))
    f = [0] * (S + 1)
    f[0] = 1
    for s in range(1, S + 1):
        for x in c:
            if x <= s:
                f[s] = (f[s] + f[s - x]) % MOD
    with open('DOITIEN.OUT', 'w') as out:
        out.write(str(f[S]) + '\n')

main()
