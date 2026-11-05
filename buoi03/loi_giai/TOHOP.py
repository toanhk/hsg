# TOHOP: liet ke to hop chap k cua {1..n} theo thu tu tu dien. De bao dam C(n, k) <= 10^5
# Quay lui: phan tu thu j (0..k-1) chay tu (phan tu truoc + 1) den n - (k - 1 - j)
# Cat nhanh: neu bat dau qua muon thi khong con du so cho cac vi tri sau -> khong bao gio vao nhanh cut
import sys

def main():
    data = open('TOHOP.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    x = [0] * k
    kq = []

    def thu(j, bat_dau):     # chon phan tu thu j, gia tri >= bat_dau
        if j == k:
            kq.append(' '.join(map(str, x)))
            return
        for v in range(bat_dau, n - (k - 1 - j) + 1):
            x[j] = v
            thu(j + 1, v + 1)

    thu(0, 1)
    with open('TOHOP.OUT', 'w') as f:
        f.write(str(len(kq)) + '\n' + '\n'.join(kq) + '\n')

main()
