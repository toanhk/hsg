# KHONGKE: chon mot so phan tu cua day a[1..n], KHONG chon 2 phan tu ke nhau, tong lon nhat.
# Duoc phep khong chon gi (tong 0). n <= 10^6, |a[i]| <= 10^9
#   Trang thai : f[i] = tong lon nhat khi chi xet a[1..i]
#   Truy hoi   : f[i] = max( f[i-1]          (khong chon a[i]),
#                            f[i-2] + a[i] ) (chon a[i] -> bat buoc bo a[i-1])
#   Khoi tao   : f[-1] = f[0] = 0
#   Thu tu     : i tang dan
#   Dap an     : f[n]
# f[i] chi can f[i-1], f[i-2] -> giu 2 bien (truoc2 = f[i-2], truoc1 = f[i-1]), khong can mang.
# Dung 'if' thay cho ham max(): goi ham trong Python ton thoi gian hon so sanh (xem do_qhd1chieu.py).
def main():
    data = open('KHONGKE.INP', 'rb').read().split()
    n = int(data[0])
    truoc2 = truoc1 = 0
    for x in map(int, data[1:1 + n]):
        chon = truoc2 + x
        truoc2 = truoc1
        if chon > truoc1:
            truoc1 = chon
    with open('KHONGKE.OUT', 'w') as out:
        out.write(str(truoc1) + '\n')

main()
