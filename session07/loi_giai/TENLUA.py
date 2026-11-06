# TENLUA: n ten lua bay toi theo thu tu, do cao h_1..h_n. Moi he thong danh chan ban phat dau o do cao
# bat ky, cac phat sau KHONG CAO HON phat truoc. (1) Mot he thong chan duoc nhieu nhat bao nhieu qua?
# (2) Can it nhat bao nhieu he thong de chan het?  n <= 2*10^5, h_i <= 10^9
# (1) = day con KHONG TANG dai nhat. Dao dau: -h khong giam -> LIS khong giam -> bisect_RIGHT.
# (2) Tham lam: moi qua giao cho he thong co "phat cuoi" thap nhat ma van >= h; khong co thi mo he thong
#     moi. Danh sach phat cuoi cua cac he thong luon TANG chat -> chinh la mang d cua LIS tang chat
#     voi bisect_LEFT. Vay (2) = do dai day con TANG CHAT dai nhat (dinh ly Dilworth).
# Hai lan duyet O(n log n) ~ 0.15 s
from bisect import bisect_left, bisect_right

def main():
    data = open('TENLUA.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    d1 = []                                 # LIS khong giam cua -h
    d2 = []                                 # LIS tang chat cua h = phat cuoi cua cac he thong
    for x in h:
        y = -x
        k = bisect_right(d1, y)
        if k == len(d1):
            d1.append(y)
        else:
            d1[k] = y
        k = bisect_left(d2, x)
        if k == len(d2):
            d2.append(x)
        else:
            d2[k] = x
    with open('TENLUA.OUT', 'w') as out:
        out.write(f'{len(d1)}\n{len(d2)}\n')

main()
