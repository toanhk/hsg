# XOA1: chon mot doan con lien tiep, duoc XOA TOI DA 1 phan tu trong doan (doan sau khi xoa phai
# con it nhat 1 phan tu). Tong lon nhat? n <= 10^6, |a[i]| <= 10^9
# Kadane voi them mot chieu nho: "da xoa chua".
#   Trang thai : f0[i] = tong lon nhat cua doan ket thuc tai i, CHUA xoa (chua a[i])
#                f1[i] = tong lon nhat cua doan ket thuc tai i, DA xoa dung 1 phan tu
#   Truy hoi   : f0[i] = a[i] + max(f0[i-1], 0)
#                f1[i] = max( f1[i-1] + a[i],   (da xoa tu truoc, giu a[i])
#                             f0[i-1] )         (xoa chinh a[i]; doan con lai ket thuc tai i-1)
#   Khoi tao   : f0[1] = a[1], f1[1] = -vo cung (xoa a[1] thi doan rong -> khong hop le)
#   Thu tu     : i tang dan; tinh f1 moi TRUOC khi ghi de f0 (vi f1 can f0[i-1])
#   Dap an     : max cua moi f0[i], f1[i]
AM_VC = -10**18

def main():
    data = open('XOA1.INP', 'rb').read().split()
    n = int(data[0])
    a = map(int, data[1:1 + n])
    f0 = tot = next(a)
    f1 = AM_VC
    for x in a:
        f1 += x
        if f0 > f1:                     # f1 = max(f1[i-1] + a[i], f0[i-1])
            f1 = f0
        if f0 > 0:                      # f0 = a[i] + max(f0[i-1], 0)
            f0 += x
        else:
            f0 = x
        if f0 > tot:
            tot = f0
        if f1 > tot:
            tot = f1
    with open('XOA1.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
