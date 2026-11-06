# NUI - ban SAI de chua bai: dung bisect_right -> thanh day "khong giam", sai khi co cay cao bang nhau.
# NUI: n cay tren mot hang, cay i cao h[i]. Chat it cay nhat de day chieu cao con lai co dang "nui":
# TANG NGAT roi GIAM NGAT (chi tang hoac chi giam cung duoc). In so cay phai chat. n <= 2*10^5
#   Trang thai : L[i] = do dai day con tang ngat dai nhat KET THUC tai i
#                R[i] = do dai day con giam ngat dai nhat BAT DAU tai i (= LIS tu phai sang)
#   Truy hoi   : L[i] = 1 + max L[j] voi j < i, h[j] < h[i]; R tuong tu tu phai
#   Khoi tao   : L[i] >= 1, R[i] >= 1
#   Thu tu     : L: i tang; R: i giam
#   Dap an     : n - max(L[i] + R[i] - 1)   (dinh nui la cay i, dem 2 lan nen tru 1)
# O(n log n): "tails[k] = chieu cao cuoi nho nhat cua day tang do dai k+1"; vi tri bisect_right
# cua h[i] trong tails chinh la L[i] - 1. BAN NAY CO TINH dung bisect_right (dung phai la bisect_left).
from bisect import bisect_right

def lis_ket_thuc(h):
    tails = []
    L = []
    for x in h:
        p = bisect_right(tails, x)          # SAI: x bang phan tu cu se noi dai day
        if p == len(tails):
            tails.append(x)
        else:
            tails[p] = x
        L.append(p + 1)
    return L

def main():
    data = open('NUI.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    L = lis_ket_thuc(h)
    R = lis_ket_thuc(h[::-1])[::-1]
    dai = max(map(lambda a, b: a + b - 1, L, R))
    with open('NUI.OUT', 'w') as f:
        f.write(str(n - dai) + '\n')

main()
