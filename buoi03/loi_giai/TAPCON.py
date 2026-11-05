# TAPCON: dem so tap con (chon theo vi tri) cua n so nguyen duong co tong dung bang S. n <= 20
# Quay lui giong TOHOP: moi loi goi chon "phan tu tiep theo" j > phan tu vua chon
#   -> moi tap con ung voi dung 1 loi goi (2^n loi goi, it hon mot nua so voi cay chon/khong chon)
# Sap xep tang dan de cat nhanh: neu tong + a[j] > S thi moi a[j'] sau cung qua -> break
def main():
    data = open('TAPCON.INP', 'rb').read().split()
    n, S = int(data[0]), int(data[1])
    a = sorted(map(int, data[2:2 + n]))
    dem = 0

    def thu(i, tong):                    # da chon xong mot tap co tong 'tong'; chon tiep tu vi tri i
        nonlocal dem
        for j in range(i, n):
            t = tong + a[j]
            if t > S:
                break                    # cat nhanh: a tang dan
            if t == S:
                dem += 1                 # khong goi tiep: them phan tu duong se vuot S
            else:
                thu(j + 1, t)

    thu(0, 0)
    with open('TAPCON.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
