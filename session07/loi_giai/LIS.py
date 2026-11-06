# LIS: do dai day con TANG CHAT dai nhat cua day a (n <= 5*10^5, |a_i| <= 10^9)
# Ban O(n log n) - "xep bai" (patience):
#   d[k] = phan tu CUOI NHO NHAT trong cac day con tang do dai k+1 da gap
#   d luon tang chat -> tim vi tri bang bisect_left (tim kiem nhi phan, viet bang C)
#   Gap x: tim k = vi tri dau tien co d[k] >= x
#          k == len(d)  -> x lon hon moi phan tu cuoi: noi dai day them 1
#          nguoc lai    -> thay d[k] = x (cung do dai k+1 nhung ket thuc nho hon, de noi tiep hon)
#   Dap an: len(d). CHU Y: d KHONG phai la mot day con tang hop le, chi co do dai la dung.
# Doi sang day KHONG GIAM: dung bisect_right thay bisect_left.
# 5*10^5 lan bisect ~ 0.15 s, doc du lieu ~ 0.1 s
from bisect import bisect_left

def main():
    data = open('LIS.INP', 'rb').read().split()
    n = int(data[0])
    a = map(int, data[1:1 + n])
    d = []
    for x in a:
        k = bisect_left(d, x)
        if k == len(d):
            d.append(x)
        else:
            d[k] = x
    with open('LIS.OUT', 'w') as out:
        out.write(str(len(d)) + '\n')

main()
