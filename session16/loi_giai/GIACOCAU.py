# GIACOCAU: n xa, m cay cau (u, v, loi ich w, t). Chi du kinh phi gia co DUNG n-1 cay cau sao cho moi xa van
# di duoc toi nhau qua cac cau duoc gia co (tuc la chon mot CAY KHUNG). Cau co t = 1 da gia co tu truoc,
# BAT BUOC phai nam trong tap chon. Tong loi ich lon nhat? Khong chon duoc thi in -1.
# n <= 10^5, m <= 2*10^5, 1 <= w <= 10^9.
# CAY KHUNG LON NHAT: Kruskal xet canh theo w GIAM DAN (doi dau so sanh, phan con lai giu nguyen).
# Canh bat buoc: hop vao DSU TRUOC moi canh khac. Neu hai canh bat buoc noi hai xa da lien thong
# -> cac canh bat buoc tao chu trinh -> khong the la cay -> -1.
# Tinh dung: sau khi "co dinh" cac canh bat buoc, Kruskal tren do thi con lai van cho cay tot nhat
# (giong nhu chap cac thanh phan bat buoc thanh mot dinh).
def main():
    data = open('GIACOCAU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    U = list(map(int, data[2:2 + 4 * m:4]))
    V = list(map(int, data[3:3 + 4 * m:4]))
    W = list(map(int, data[4:4 + 4 * m:4]))
    T = data[5:5 + 4 * m:4]                    # giu dang bytes: b'1' / b'0'
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    # thu tu xet: canh bat buoc truoc, roi canh tu chon theo w giam dan
    bat_buoc = [i for i in range(m) if T[i] == b'1']
    tu_chon = sorted((i for i in range(m) if T[i] != b'1'), key=W.__getitem__, reverse=True)
    tong = 0; chon = 0; hong = False
    for i in bat_buoc + tu_chon:
        a = U[i]
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        b = V[i]
        while parent[b] != b:
            parent[b] = parent[parent[b]]; b = parent[b]
        if a == b:
            if T[i] == b'1':
                hong = True                    # canh bat buoc tao chu trinh
                break
            continue
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a; size[a] += size[b]
        tong += W[i]; chon += 1
    with open('GIACOCAU.OUT', 'w') as f:
        f.write(str(-1 if hong or chon != n - 1 else tong) + '\n')

main()
